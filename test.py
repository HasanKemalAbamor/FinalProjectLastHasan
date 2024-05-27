import matplotlib.pyplot as plt
import numpy as np

# Sample data (numeric values only, excluding the initial ID and final "ok" values)
data = "0.47966889264215,0.47742324048705,0.48795608071738,0.49183077800899,0.50051621034369,0.50258968957775,0.51156076159836,0.51463932321816,0.52424521653144,0.53616993840094,0.54640701683244,0.561556554537,0.56841724231253,0.5718772477893,0.57088432832582,0.56903220048707,0.56747605052152,0.56566229266352,0.56190093874244,0.55972220729913,0.5574740460291,0.55437135838352,0.55238602526318,0.54870205531903,0.54423841292138,0.54257948065158,0.54051385228839,0.53898044296475,0.53664952597192,0.53648323613912,0.5354469681512,0.53757684192103,0.53571526530775,0.53689464592079,0.53958905251472,0.541080656254,0.54489301169844,0.54776465366844,0.55177321005769,0.55459903447976,0.56129040860412,0.5663270595839,0.57256146352886,0.58405797466784,0.60059863597386,0.62307008254835,0.65828547764517,0.68611422119961,0.70954450447026,0.72482082889484,0.73498761015134,0.74178082001324,0.74743557847871,0.75143550890412,0.75442243371844,0.75645261908949,0.7575512530684,0.75590589327176,0.75531152477726,0.75368332703197,0.74948522338108,0.74708913203127,0.74236520002832,0.73780079144338,0.73179960432508,0.72890103045345,0.72666493926652,0.72498736432713,0.72323572673202,0.72221802601647,0.72195899659511,0.72341962878724,0.72556768887055,0.72791164164271,0.73280767589074,0.73884059897309,0.7441956852289,0.75093610605003,0.7604593437847,0.77115507667331,0.78699005300512,0.80256677108113,0.82015119540574,0.8403852787303,0.86242799159858,0.88398695840413,0.91502243931015,0.93812142835335,0.96213389416547,0.98511046535052,1.0053756761573,1.0281668914297,1.0576725529044,1.0912360535355,1.1315551576365,1.1832930596264,1.2506288606325,1.3470671116531,1.4341026497277,1.5139079112707,1.5807632864563,1.6336620579284,1.6820373057844,1.7139567667587,1.7266142972209,1.7483431988319,1.7479452461472,1.7585692981057,1.7669213852563,1.769584477422,1.7799195151686,1.7753197707142,1.7780082228767,1.7719922996674,1.7693436786974,1.7603722366552,1.758964295165,1.7406551266743,1.7257679649469,1.7313943325003,1.7086595464657,1.6880873183794,1.6751667051508,1.6720704134994,1.6543357523809,1.6389993755083,1.6251878376529,1.606235202966,1.5891533418385,1.572245412458,1.562602286291,1.5325260438939,1.5211397275789,1.5060309744765,1.4891657177161,1.4698378250759,1.4626174518621,1.4456960708894,1.4355860674245,1.4178471593692,1.4042048948435,1.388861102272,1.3774359081585,1.3644440460745,1.3603729523446,1.3412425763255,1.3396319151792,1.3214709525501,1.3174440791675,1.3112087203946,1.2916769550509,1.2855791553561,1.2854879187059,1.2757844247449,1.2711039216371,1.2640289400139,1.2507785003118,1.2548564518249,1.2552242308326,1.2496230691567,1.2444193629011,1.2444367438789,1.2439330440822,1.226789702688,1.2340550021974,1.2186599868674,1.2130378499155,1.198316797239,1.1957353893045,1.1808460085619,42.51,34.01"

# Convert the data to a list of floats
data_list = [float(value) for value in data.split(',')]

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(data_list, marker='o')
plt.title('Data Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# Save the plot as an image
graph_image_path = 'data_plot.png'
plt.savefig(graph_image_path)
plt.close()

print(f"Graph image saved as '{graph_image_path}'")