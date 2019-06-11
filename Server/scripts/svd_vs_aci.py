import main
import matplotlib.pyplot as plt
import data_creation


acis = []
scores = []

for i in range(20) :
    data_creation.create_data(10,80)
    aci, score = main.compute()
    print(aci, score)
    acis.append(aci)
    scores.append(score)

# plt.plot(scores, acis)
plt.scatter(scores, acis)
plt.show()
