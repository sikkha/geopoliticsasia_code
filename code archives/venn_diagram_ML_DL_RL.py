iimport matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sizes of the three sets and their overlaps
ML = 300
DL = 300
RL = 300
ML_DL = 100
DL_RL = 100
ML_RL = 100
all_three = 50

# Set the figure size
plt.figure(figsize=(10, 10))

# Create the Venn diagram
venn = venn3(subsets=(ML, DL, RL, ML_DL, DL_RL, ML_RL, all_three),
             set_labels=('', '', ''),
             subset_label_formatter=lambda x: '')

# Customize the colors and labels
venn.get_label_by_id('100').set_text('Machine\nLearning')
venn.get_label_by_id('010').set_text('Deep\nLearning')
venn.get_label_by_id('001').set_text('Reinforcement\nLearning')
venn.get_patch_by_id('100').set_color('lightblue')
venn.get_patch_by_id('010').set_color('lightcoral')
venn.get_patch_by_id('001').set_color('lightgreen')

# Add labels to the intersection areas
label_position_110 = venn.get_label_by_id('110').get_position()
plt.annotate('Artificial Neural Networks', xy=(label_position_110[0], label_position_110[1] + 0.03), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)
plt.annotate('Convolutional Neural Networks', xy=(label_position_110[0], label_position_110[1] - 0.02), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)
plt.annotate('Recurrent Neural Networks', xy=(label_position_110[0], label_position_110[1] - 0.07), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)

label_position_011 = venn.get_label_by_id('011').get_position()
plt.annotate('Deep Neural Networks', xy=(label_position_011[0], label_position_011[1] - 0.02), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)

label_position_101 = venn.get_label_by_id('101').get_position()
plt.annotate('Q-learning and SARSA', xy=(label_position_101[0], label_position_101[1] + 0.03), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)

label_position_111 = venn.get_label_by_id('111').get_position()
plt.annotate('Generative Adversarial Networks (GANs)', xy=(label_position_111[0], label_position_111[1]), xytext=(10, 0), textcoords='offset points', ha='center', fontsize=9)

# Display the Venn diagram
plt.title("Learning Algorithm Universe")
plt.show()

