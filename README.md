# Writeup: Track 3D-Objects Over Time

### Step 1 - Implemented the Kalman Filter
The predict function was completed by implementing the functions F and Q and the update function was completed by implementing the functions Gamma and S.

Below is the RMSE plot for a single track after this step:
![alt text](https://github.com/shirvonp/sensor_fusion/blob/main/RMSE_Step_1.png)

### Step 2 - Track Management 
For this step the track management class was completed, it is responsible for initialization, confirmation, deleting and updating of states of given tracks. This step took the longest to complete as it took some time to figure out the correct method to delete and confirm tracks.

Below is the RMSE plot after completing step 2:
![alt text](https://github.com/shirvonp/sensor_fusion/blob/main/RMSE_Step_2.png)

### Step 3 - Association
This step we associate new measurements with current tracks using the Mahalanobis distance and gating functions.

Below is the RMSE plot after completing step 3:
![alt text](https://github.com/shirvonp/sensor_fusion/blob/main/RMSE_Step_3.png)

### Step 3 - Camera-Lidar Fusion
To include the camera data the non-linear measurement function get_hx(x) needed to be implemented.

Below is the RMSE plot after completing step 4:
![alt text](https://github.com/shirvonp/sensor_fusion/blob/main/RMSE_Step_4.png)
