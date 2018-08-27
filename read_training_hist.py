import numpy as np

history = np.load('./output/trained_data.npy').item()
mat = np.append(np.append(np.append(history['acc'], history['val_acc']), history['loss']), history['val_loss'])
np.savetxt('mat.csv', mat)