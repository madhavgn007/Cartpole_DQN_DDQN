from src.DQN.DQNAgent import DQNAgent
from src.DDQN.DDQNAgent import DDQNAgent
import numpy as np

######################################################################################################
###################################---DQNAgent and DDQNAgent Initialization---########################
######################################################################################################

dqn_agent = DQNAgent()  # Create DQNAgent instance
ddqn_agent = DDQNAgent()  # Create DDQNAgent instance

######################################################################################################
################################---Testing DQNAgent and DDQNAgent---##################################
######################################################################################################

dqn_agent.test("dqn", 20)  # Test DQNAgent
ddqn_agent.test("ddqn", 20)  # Test DDQNAgent

######################################################################################################
############################---Mean Scores DQNAgent and DDQNAgent---##################################
######################################################################################################

print('###############################################################################################')
print(f'DQN testing terminated with an average of {np.mean(dqn_agent.test_scores)} over 20 episodes')
print('###############################################################################################')

print('###############################################################################################')
print(f'DDQN testing terminated with an average of {np.mean(ddqn_agent.test_scores)} over 20 episodes')
print('###############################################################################################')