from process_text import *
from generators import GeneralGenerator
from generators import GeneralGenerator
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.models import load_model


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def build_model(len_voc, max_len = 100, embedding_dim = 300):
    # build the model: a single LSTM
    print('Build model...')
    model = Sequential()
    model.add(Embedding(input_dim=len_voc+1, output_dim=embedding_dim, input_length=max_len, mask_zero=True))
    model.add(LSTM(128))
    model.add(Dense(len(voc)))
    model.add(Activation('softmax'))
    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model


def run_model(model, ind_corpus_train, voc, epochs = 60, batch_size = 128, max_len= 100):
    # train model
    train_gen = GeneralGenerator(batch_size, ind_corpus_train, voc, max_len)

    print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

    model_output = model.fit_generator(
        train_gen.generator(),
        train_gen.steps_per_epoch,
        epochs=epochs#,
        #callbacks=[print_callback]
    )
    return model

def main():
    train_raw_filename ='./data/horoscopo_raw.txt' 
    test_raw_filename = './data/horoscopo_raw.txt'

    corpus_train = open(train_raw_filename).read().lower()[1:1000]
    corpus_test = open(test_raw_filename).read().lower()[1:1000]

    for a in range(11):
        quantity_syllable = a/10.0
        quantity_word = 1-a/10.0

        print('\nquantity of syllable = {} ; quantity of words = {}'.format(quantity_syllable, quantity_word))
        print('Process text...')
        selectors = get_selectors(corpus_train, quantity_word, quantity_syllable)
        string_tokens = get_processed_text(corpus_train, selectors)
        print('tokens length:', len(string_tokens))
        # crear diccionario tokens-int
        print('Vectorization...')
        string_voc = set(string_tokens)
        token_to_index = dict((t, i) for i, t in enumerate(string_voc, 1))
        index_to_token = dict((token_to_index[t], t) for t in string_voc)
        # traducir corpus a enteros
        ind_corpus = [token_to_index[token] for token in string_tokens]
        voc = set(ind_corpus)
        print('voc size:', len(voc))


        ## build model
        model = build_model(len_voc= len(voc))

        ## run model
        model = run_model(model, ind_corpus, voc)

        ppl = test_eval(model, index_to_token, corpus_test, selectors, step_t = 100)
        print('perplexity = {} para el modelo: %palabras = {} ; %caracteres = {}'.format(ppl,quantity_word, quantity_syllable))


if __name__ == '__main__':
    main()