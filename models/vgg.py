from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


def vgg16():
    model = Sequential()
    model.add(Conv2D(64, 3, strides=(1, 1), padding="same",
                     activation="relu", input_shape=(224, 224, 3)))
    model.add(Conv2D(64, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(128, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(128, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Flatten())
    model.add(Dense(4096))
    model.add(Dense(4096))
    model.add(Dense(1000))
    return model


def vgg19():
    model = Sequential()
    model.add(Conv2D(64, 3, strides=(1, 1), padding="same",
                     activation="relu", input_shape=(224, 224, 3)))
    model.add(Conv2D(64, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(128, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(128, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(256, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(Conv2D(512, 3, strides=(1, 1), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
    model.add(Flatten())
    model.add(Dense(4096))
    model.add(Dense(4096))
    model.add(Dense(1000))
    return model


if __name__ == "__main__":
    vgg16().summary()
    vgg19().summary()
