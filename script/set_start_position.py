import vrep
import time

#Posicao inicial de cada parte do robo
#***************************************/
#Head
#***************************************/

#HeadYawLink
HeadYawLinkPosition = [1.8715858459472656e-05, 8.955597877502441e-06, -9.098649024963379e-05]
HeadYawLinkOrientation = [-6.09556955168955e-05, 0.0005293078138493001, -1.36396383823012e-05]

#HeadPitchLink
HeadPitchLinkPosition = [0.0013996362686157227, -0.061526596546173096, -6.020069122314453e-05]
HeadPitchLinkOrientation = [1.5707972049713135, 2.030277528319857e-07, 1.3273301192384679e-05]

#***************************************/
#***Right Leg
#***************************************/

#RHipRollLink
RHipRollLinkPosition = [-0.017775297164916992, -0.001258552074432373, 0.019459417089819908]
RHipRollLinkOrientation =[0.7853147983551025, -0.0002430556487524882, -5.049790161137935e-06]

#RHipRollLink2
RHipRollLink2Position = [0.008198589086532593, -1.1742115020751953e-05, -0.00920403003692627]
RHipRollLink2Orientation = [-2.883943557739258, -1.5663613080978394, -2.8839547634124756]

#Thigh
RThighPosition = [0.0036319494247436523, 0.05186697840690613, -0.003946959972381592]
RThighOrientation = [1.5710488557815552, -0.004644586704671383, -1.7428339560865425e-05]

#Shin
RShinPosition = [0.0052754878997802734, 0.051765620708465576, -0.0050611793994903564]
RShinOrientation = [1.5708376169204712, 2.4694483613529883e-07, -8.345642709173262e-05]

#RAnklePitchLink
RAnklePitchLinkPosition = [-0.0022939443588256836, -0.013433616608381271, -0.00015923380851745605]
RAnklePitchLinkOrientation = [1.5708897113800049, -0.0008970284834504128, 1.309994246412316e-07] 

#RFoot
RFootPosition = [0.03755037486553192, 1.0460615158081055e-05, 0.020059585571289062]
RFootOrientation = [0.0, -1.5696003437042236, 5.440803761302959e-06]

#RFootPiece1
RFootPiece1Position = [1.1682510375976562e-05, 3.069639205932617e-06, 0.0002448330633342266]
RFootPiece1Orientation = [8.545499440515414e-05, -0.0001614848879398778, 9.016980584419798e-07]

#RFootPiece2
RFootPiece2Position = [6.9141387939453125e-06, -1.4901161193847656e-07, 0.0002772319130599499]
RFootPiece2Orientation = [-3.1710857001598924e-05, -0.0003417811240069568, -1.1263565511399065e-06] 

#RFootPiece3
RFootPiece3Position = [7.748603820800781e-06, 6.407499313354492e-07, 0.00024244468659162521]
RFootPiece3Orientation = [0.00033434067154303193, -0.0001033588414429687, 1.0477391697349958e-05] 

#RFootPiece4
RFootPiece4Position = [4.5299530029296875e-06, 6.407499313354492e-07, 0.0002804533578455448]
RFootPiece4Orientation = [0.00017455413762945682, -0.0002107644540956244, -6.735291208315175e-06]

#***************************************/
#Left Leg
#***************************************/

#LHipRollLink
LHipRollLinkPosition = [-0.01778721809387207, -0.0011631213128566742, -0.019540607929229736]
LHipRollLinkOrientation = [2.356175661087036, -4.696758696809411e-05, -7.384680793620646e-05]

#LHipRollLink2
LHipRollLink2Position = [0.008206173777580261, -3.454089164733887e-05, -0.00920569896697998]
LHipRollLink2Orientation = [2.8937199115753174, -1.5663882493972778, 2.8937530517578125]

#Thigh
LThighPosition = [0.0036324262619018555, 0.051872313022613525, 0.0039010941982269287]
LThighOrientation = [1.5705314874649048, -0.004652504343539476, 2.445421887387056e-05]

#Shin
LShinPosition = [0.005275845527648926, 0.05229046195745468, 0.005012825131416321]
LShinOrientation = [1.5707480907440186, 2.6061172775371233e-07, 0.0001014571898849681]

#LAnklePitchLink
LAnklePitchLinkPosition = [-0.0022928714752197266, -0.013432476669549942, 0.00014819204807281494]
LAnklePitchLinkOrientation = [1.5706698894500732, -0.0008977077668532729, -1.6173809171959874e-06]

#LFoot
LFootPosition = [0.03755294159054756, -2.2277235984802246e-05, 0.02005934715270996]
LFootOrientation = [0.0, -1.5695514678955078, -4.2557343249427504e-07]

#LFootPiece1
LFootPiece1Position = [5.364418029785156e-06, 5.424022674560547e-06, 0.0002401578240096569]
LFootPiece1Orientation = [-0.0004836999869439751, 8.518587492289953e-06, 2.8496615414042026e-06]

#LFootPiece2
LFootPiece2Position = [1.1801719665527344e-05, 3.7550926208496094e-06, 0.00029570097103714943]
LFootPiece2Orientation = [-0.00021044525783509016, -0.0002815594198182225, -5.86819169257069e-06]

#LFootPiece3
LFootPiece3Position = [1.049041748046875e-05, 5.736947059631348e-06, 0.0002265293151140213]
LFootPiece3Orientation = [-0.00026060533127747476, -7.238696707645431e-05, -1.0841739822353702e-05]

#LFootPiece4
LFootPiece4Position = [8.463859558105469e-06, 4.3138861656188965e-06, 0.0002553798258304596]
LFootPiece4Orientation = [-0.0004960412043146789, -6.60947262076661e-05, -4.1667067307571415e-06]


#***************************************/
#***Right Arm
#***************************************/

#RShoulderPitchLink
RShoulderPitchLinkPosition = [-9.417533874511719e-06, 4.9173831939697266e-06, 7.748603820800781e-07]
RShoulderPitchLinkOrientation = [1.5707975625991821, -1.935233342464926e-07, 7.710120257797826e-07]

#RShoulderRollLink
RShoulderRollLinkPosition = [0.03748452663421631, -0.0069029927253723145, -0.001744091510772705]
RShoulderRollLinkOrientation = [0.006057446822524071, 0.04075365141034126, -6.017977648298256e-05]

#RElbowYawLink
RElbowYawLinkPosition = [0.00010570883750915527, -8.940696716308594e-07, 3.933906555175781e-06]
RElbowYawLinkOrientation = [-0.27350053191185, -1.5668597221374512, -0.27353617548942566]

#RElbowRollLink
RElbowRollLinkPosition = [0.02172219753265381, -0.0015685856342315674, 0.0029544830322265625]
RElbowRollLinkOrientation = [-0.002734431065618992, 0.00019816370331682265, 7.78817502578022e-06]

#RWristYawLinkPosition
RWristYawLinkPosition = [-0.00021335482597351074, 0.0006688237190246582, 0.041185736656188965]
RWristYawLinkOrientation = [0.0, -1.5691404342651367, -0.03490076959133148]

NAO_RThumbBasePosition = [0.025944024324417114, 0.21813715994358063, 0.05784940719604492]
NAO_RThumbBaseOrientation = [1.6292920112609863, 0.0033585387282073498, 2.9834370613098145]

Revolute_joint0Position = [-0.011755868792533875, -0.008364439010620117, 1.84476375579834e-05]
Revolute_joint0Orientation = [0.004840541165322065, 0.0077466899529099464, 0.05360434949398041]

NAO_RLFingerBasePosition = [0.0030570030212402344, 0.2286110669374466, 0.07839441299438477] 
NAO_RLFingerBaseOrientation = [-1.4882774353027344, -0.1624104082584381, 2.1360397338867188]

Revolute_joint5Position = [0.010773539543151855, 0.00956261157989502, -3.1054019927978516e-05]
Revolute_joint5Orientation = [0.0002961151476483792, 0.0006809839978814125, 0.00010974091856041923]

Revolute_joint6Position = [0.010578334331512451, 0.009820818901062012, -5.3495168685913086e-05]
Revolute_joint6Orientation = [-0.006720967590808868, -0.007421066518872976, 0.08294139057397842]

NAO_RRFinger_BasePosition = [-5.269466876983643, 0.8754734992980957, 1.0583794116973877]
NAO_RRFinger_BaseOrientation = [0.7563453316688538, 1.4945223331451416, -0.7447685599327087]

Revolute_joint2Position = [1.2596853971481323, -0.6260848045349121, 5.24915885925293]
Revolute_joint2Orientation = [-1.4559403657913208, 0.03167594596743584, 2.794023275375366]

Revolute_joint3Position = [0.01308751106262207, 0.005975544452667236, 4.673004150390625e-05]
Revolute_joint3Orientation = [-0.007444398012012243, -0.00891663134098053, -0.23325411975383759]



#***************************************/
#***Left Arm
#***************************************/


#LShoulderPitchLink
LShoulderPitchLinkPosition = [1.9073486328125e-06, 2.5540590286254883e-05, 6.847083568572998e-06]
LShoulderPitchLinkOrientation = [1.570695161819458, 0.00025133928284049034, -5.0871290113718715e-06]

#LShoulderRollLink
LShoulderRollLinkPosition = [0.03724968433380127, 0.0069495514035224915, -0.0016518831253051758]
LShoulderRollLinkOrientation = [-0.006304544862359762, 0.04182317107915878, -4.268097472959198e-05]

#LElbowYawLink
LElbowYawLinkPosition = [3.466010093688965e-05, 3.5762786865234375e-07, 4.76837158203125e-07]
LElbowYawLinkOrientation = [0.0, -1.5707963705062866, 1.4716455484786728e-11]

#LElbowRollLink
LElbowRollLinkPosition = [0.0217362642288208, 0.0015653818845748901, 0.002849489450454712]
LElbowRollLinkOrientation = [0.00350018753670156, 0.002864307025447488, -1.3655902876053005e-05]

#LWristYawLinkPosition
LWristYawLinkPosition = [-0.0004229247570037842, -0.0007213354110717773, 0.04202854633331299]
LWristYawLinkOrientation = [0.0, -1.5691049098968506, 0.034898921847343445]

NAO_LThumbBasePosition = [0.025953739881515503, -0.21820175647735596, 0.05696690082550049]
NAO_LThumbBaseOrientation = [1.5123231410980225, -0.0034882482141256332, 2.9225475788116455]

Revolute_joint8Position = [-0.011755868792533875, -0.008364439010620117, 1.84476375579834e-05]
Revolute_joint8Orientation = [0.004840541165322065, 0.0077466899529099464, 0.05360434949398041]

NAO_LLFingerBasePosition = [0.002581775188446045, -0.20575308799743652, 0.0762484073638916]
NAO_LLFingerBaseOrientation = [-1.6544291973114014, -0.18631726503372192, -2.300638437271118]

Revolute_joint12Position = [0.010773539543151855, 0.00956261157989502, -3.1054019927978516e-05]
Revolute_joint12Orientation = [0.0002961151476483792, 0.0006809839978814125, 0.00010974091856041923]

Revolute_joint14Position = [0.010578334331512451, 0.009820818901062012, -5.3495168685913086e-05]
Revolute_joint14Orientation = [-0.006720967590808868, -0.007421066518872976, 0.08294139057397842]

NAO_LRFinger_BasePosition = [-5.273959159851074, 0.6986212730407715, 1.0010974407196045]
NAO_LRFinger_BaseOrientation = [0.630199134349823, 1.4975279569625854, -0.6887720227241516]

Revolute_joint11Position = [1.2596853971481323, -0.6260848045349121, 5.24915885925293]
Revolute_joint11Orientation = [-1.4559403657913208, 0.03167594596743584, 2.794023275375366]

Revolute_joint13Position = [0.01308751106262207, 0.005975544452667236, 4.673004150390625e-05]
Revolute_joint13Orientation = [-0.007444398012012243, -0.00891663134098053, -0.23325411975383759]


def get_all_handles_start(clientID,Robo, Body):

    #Robo
    Robo.append(vrep.simxGetObjectHandle(clientID,'NAO',vrep.simx_opmode_oneshot_wait)[1])

    #Head
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw_link_respondable',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadYaw',vrep.simx_opmode_oneshot_wait)[1])
    Body[2].append(vrep.simxGetObjectHandle(clientID,'HeadPitch_link_respondable',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'HeadPitch',vrep.simx_opmode_oneshot_wait)[1])

    #Left Leg
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'l_hip_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'l_hip_roll_link_respondable4',vrep.simx_opmode_oneshot_wait)[1])
    Body[8].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'l_hip_pitch_pure2',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'l_knee_pitch_link_pure2',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'l_ankle_pitch_link_pure3',vrep.simx_opmode_oneshot_wait)[1])
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'l_ankle_link_pure3',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'NAO_LFsrRR',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure5',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'NAO_LFsrFR',vrep.simx_opmode_oneshot_wait)[1])
    Body[19].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure6',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'NAO_LFsrRL',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure7',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'NAO_LFsrFL',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure8',vrep.simx_opmode_oneshot_wait)[1])

   
    #Right Leg
    Body[24].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(vrep.simxGetObjectHandle(clientID,'r_hip_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(vrep.simxGetObjectHandle(clientID,'r_hip_roll_link_respondable5',vrep.simx_opmode_oneshot_wait)[1])
    Body[28].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[29].append(vrep.simxGetObjectHandle(clientID,'r_hip_pitch_pure2',vrep.simx_opmode_oneshot_wait)[1])
    Body[30].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[31].append(vrep.simxGetObjectHandle(clientID,'r_knee_pitch_link_pure2',vrep.simx_opmode_oneshot_wait)[1])
    Body[32].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[33].append(vrep.simxGetObjectHandle(clientID,'r_ankle_pitch_link_pure3',vrep.simx_opmode_oneshot_wait)[1])
    Body[34].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[35].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure9',vrep.simx_opmode_oneshot_wait)[1])
    Body[36].append(vrep.simxGetObjectHandle(clientID,'NAO_RFsrRR',vrep.simx_opmode_oneshot_wait)[1])
    Body[37].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure3',vrep.simx_opmode_oneshot_wait)[1])
    Body[38].append(vrep.simxGetObjectHandle(clientID,'NAO_RFsrFR',vrep.simx_opmode_oneshot_wait)[1])
    Body[39].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure2',vrep.simx_opmode_oneshot_wait)[1])
    Body[40].append(vrep.simxGetObjectHandle(clientID,'NAO_RFsrRL',vrep.simx_opmode_oneshot_wait)[1])
    Body[41].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure0',vrep.simx_opmode_oneshot_wait)[1])
    Body[42].append(vrep.simxGetObjectHandle(clientID,'NAO_RFsrFL',vrep.simx_opmode_oneshot_wait)[1])
    Body[43].append(vrep.simxGetObjectHandle(clientID,'r_sole_link_pure1',vrep.simx_opmode_oneshot_wait)[1])


   #Right Arm
    Body[44].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[45].append(vrep.simxGetObjectHandle(clientID,'r_shoulder_pitch_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[46].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[47].append(vrep.simxGetObjectHandle(clientID,'r_shoulder_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[48].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3',vrep.simx_opmode_oneshot_wait)[1])
    Body[49].append(vrep.simxGetObjectHandle(clientID,'r_elbow_yaw_link_respondable1',vrep.simx_opmode_oneshot_wait)[1])
    Body[50].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[51].append(vrep.simxGetObjectHandle(clientID,'r_elbow_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[52].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3',vrep.simx_opmode_oneshot_wait)[1])
    Body[53].append(vrep.simxGetObjectHandle(clientID,'r_wrist_yaw_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
 

   #Left Arm
    Body[54].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3',vrep.simx_opmode_oneshot_wait)[1])
    Body[55].append(vrep.simxGetObjectHandle(clientID,'l_shoulder_pitch_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[56].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[57].append(vrep.simxGetObjectHandle(clientID,'l_shoulder_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[58].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3',vrep.simx_opmode_oneshot_wait)[1])
    Body[59].append(vrep.simxGetObjectHandle(clientID,'l_elbow_yaw_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[60].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3',vrep.simx_opmode_oneshot_wait)[1])
    Body[61].append(vrep.simxGetObjectHandle(clientID,'l_elbow_roll_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    Body[62].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3',vrep.simx_opmode_oneshot_wait)[1])
    Body[63].append(vrep.simxGetObjectHandle(clientID,'l_wrist_yaw_link_respondable3',vrep.simx_opmode_oneshot_wait)[1])
    
    #Left Fingers
    Body[64].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11',vrep.simx_opmode_oneshot_wait)[1])
    Body[64].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13',vrep.simx_opmode_oneshot_wait)[1])
    Body[65].append(Body[64][0:8])

    #Right Fingers
    Body[66].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2',vrep.simx_opmode_oneshot_wait)[1])
    Body[66].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3',vrep.simx_opmode_oneshot_wait)[1])
    Body[67].append(Body[66][0:8])




#def setStartPosition(clientID, PositionZero, OrientationZero):
#def setStartPosition(clientID, PositionZero):
def setStartPosition(clientID):
    #Robo
    Robo=[];
    
    #Head
    HeadYawLink=[];        HeadYaw=[];  HeadPitchLink=[]; HeadPitch=[];
    
    #Left Leg
    LHipYawPitch=[];    LHipRollLink=[];    LHipRoll3=[];   LHipRollLink2=[];   LHipPitch3=[];
    LThigh=[];          LKneePitch3=[];     LShin=[];       LAnklePitch3=[];    LAnklePitchLink=[];
    LAnkleRoll3=[];     LFoot=[];           NAO_LFsrRR=[];  LFootPiece1=[];     NAO_LFsrFR=[];
    LFootPiece2=[];     NAO_LFsrRL=[];      LFootPiece3=[]; NAO_LFsrFL=[];      LFootPiece4=[];
    
    #Right Leg
    RHipYawPitch=[];    RHipRollLink=[];    RHipRoll3=[];   RHipRollLink2=[];   RHipPitch3=[];
    RThigh=[];          RKneePitch3=[];     RShin=[];       RAnklePitch3=[];    RAnklePitchLink=[];
    RAnkleRoll3=[];     RFoot=[];           NAO_RFsrRR=[];  RFootPiece1=[];     NAO_RFsrFR=[];
    RFootPiece2=[];     NAO_RFsrRL=[];      RFootPiece3=[]; NAO_RFsrFL=[];      RFootPiece4=[];

    #Right Arm
    RShoulderPitch=[];  RShoulderPitchLink=[];  RShoulderRoll=[];   RShoulderRollLink=[];   RElbowYaw=[];
    RElbowYawLink=[];   RElbowRoll=[];          RElbowRollLink=[];  RWristYaw=[];           RWristYawLink=[];

    #Left Arm
    LShoulderPitch=[];  LShoulderPitchLink=[];  LShoulderRoll=[];   LShoulderRollLink=[];   LElbowYaw=[];
    LElbowYawLink=[];   LElbowRoll=[];          LElbowRollLink=[];  LWristYaw=[];           LWristYawLink=[];
    
    R_H=[];             L_Hand=[];             L_H=[];             R_Hand=[];

    Body = [HeadYawLink,HeadYaw,HeadPitchLink,HeadPitch,
            LHipYawPitch,LHipRollLink,LHipRoll3,LHipRollLink2,LHipPitch3,LThigh,LKneePitch3,LShin,LAnklePitch3,LAnklePitchLink,
            LAnkleRoll3,LFoot,NAO_LFsrRR,LFootPiece1,NAO_LFsrFR,LFootPiece2,NAO_LFsrRL,LFootPiece3,NAO_LFsrFL,LFootPiece4,
            RHipYawPitch,RHipRollLink,RHipRoll3,RHipRollLink2,RHipPitch3,RThigh,RKneePitch3,RShin,RAnklePitch3,RAnklePitchLink,
            RAnkleRoll3,RFoot,NAO_RFsrRR,RFootPiece1,NAO_RFsrFR,RFootPiece2,NAO_RFsrRL,RFootPiece3,NAO_RFsrFL,RFootPiece4,
            RShoulderPitch,RShoulderPitchLink,RShoulderRoll,RShoulderRollLink,RElbowYaw,RElbowYawLink,RElbowRoll,RElbowRollLink,RWristYaw,RWristYawLink,
            LShoulderPitch,LShoulderPitchLink,LShoulderRoll,LShoulderRollLink,LElbowYaw,LElbowYawLink,LElbowRoll,LElbowRollLink,LWristYaw,LWristYawLink,L_H,L_Hand,R_H,R_Hand]
    
    get_all_handles_start(clientID,Robo, Body)
    
    #print Body
    
    #COLOCA O ROBO NA POSICAO INICIAL
    #Motores
    vrep.simxSetJointTargetPosition(clientID,HeadYaw[0],-1.5887246263446286e-05,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,HeadPitch[0],-4.5913433055488895e-09,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RHipPitch3[0],-0.00468195416033268,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RHipRoll3[0],-0.0010810031089931726,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RHipYawPitch[0],-0.0001713628153083846,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RKneePitch3[0],4.301075762214168e-08,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RAnklePitch3[0],-0.000912433722987771,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RAnkleRoll3[0],0.00020209321519359946,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LHipPitch3[0],-0.004688275046646595, vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LHipRoll3[0],0.0010261177085340023,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LHipYawPitch[0],2.0628947822842747e-05,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LKneePitch3[0],2.956727840341955e-08,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LAnklePitch3[0],-0.0009522095206193626,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LAnkleRoll3[0],-0.00047030881978571415,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RShoulderPitch[0],-2.26113638923664e-09,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RShoulderRoll[0],-0.00039565435145050287,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RElbowRoll[0],0.034906547516584396,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RElbowYaw[0],-0.0010774648981168866,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,RWristYaw[0],-0.000519772816915065,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LShoulderPitch[0],0.00025163363898172975,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LShoulderRoll[0],0.0001892289874376729,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LElbowRoll[0],-0.03492220491170883,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LElbowYaw[0],-2.6815111242584067e-10,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,LWristYaw[0],0.000519521941896528,vrep.simx_opmode_oneshot_wait)
    

    #Right Fingers
    vrep.simxSetJointTargetPosition(clientID,R_H[0],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[1],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[2],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[3],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[4],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[5],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[6],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,R_H[7],0,vrep.simx_opmode_oneshot_wait)
    #Right Fingers
    vrep.simxSetJointTargetPosition(clientID,L_H[0],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[1],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[2],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[3],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[4],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[5],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[6],0,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetPosition(clientID,L_H[7],0,vrep.simx_opmode_oneshot_wait)
    

    time.sleep(7)
    
    #Robo
    PositionZero = [-1.7514702081680298, -0.20124384760856628, 0.35096418857574463] 

    OrientationZero = [0.00036795390769839287, 0.011648043058812618, -0.0006550566758960485]
    returnCode = vrep.simxSetObjectPosition(clientID,Robo[0],-1,PositionZero,vrep.simx_opmode_oneshot_wait)
    print returnCode 
    returnCode  = vrep.simxSetObjectOrientation(clientID,Robo[0],-1,OrientationZero,vrep.simx_opmode_oneshot_wait)
    print returnCode
    
    #This if is here just to help comment the code below when debugging
    if True:
        #Head
        vrep.simxSetObjectPosition(clientID,HeadYawLink[0],HeadYaw[0],HeadYawLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,HeadYawLink[0],HeadYaw[0],HeadYawLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,HeadPitchLink[0],HeadPitch[0],HeadPitchLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,HeadPitchLink[0],HeadPitch[0],HeadPitchLinkOrientation,vrep.simx_opmode_oneshot_wait)
    
    
        #Right Leg
        vrep.simxSetObjectPosition(clientID,RHipRollLink[0],RHipYawPitch[0],RHipRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RHipRollLink[0],RHipYawPitch[0],RHipRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RHipRollLink2[0],RHipRoll3[0],RHipRollLink2Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RHipRollLink2[0],RHipRoll3[0],RHipRollLink2Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RThigh[0],RHipPitch3[0],RThighPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RThigh[0],RHipPitch3[0],RThighOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RShin[0],RKneePitch3[0],RShinPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RShin[0],RKneePitch3[0],RShinOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RAnklePitchLink[0],RAnklePitch3[0],RAnklePitchLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RAnklePitchLink[0],RAnklePitch3[0],RAnklePitchLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RFoot[0],RAnkleRoll3[0],RFootPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RFoot[0],RAnkleRoll3[0],RFootOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RFootPiece1[0],NAO_RFsrRR[0],RFootPiece1Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RFootPiece1[0],NAO_RFsrRR[0],RFootPiece1Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RFootPiece2[0],NAO_RFsrFR[0],RFootPiece2Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RFootPiece2[0],NAO_RFsrFR[0],RFootPiece2Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RFootPiece3[0],NAO_RFsrRL[0],RFootPiece3Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RFootPiece3[0],NAO_RFsrRL[0],RFootPiece3Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RFootPiece4[0],NAO_RFsrFL[0],RFootPiece4Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RFootPiece4[0],NAO_RFsrFL[0],RFootPiece4Orientation,vrep.simx_opmode_oneshot_wait)
        
        #Left Leg
        vrep.simxSetObjectPosition(clientID,LHipRollLink[0],LHipYawPitch[0],LHipRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LHipRollLink[0],LHipYawPitch[0],LHipRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LHipRollLink2[0],LHipRoll3[0],LHipRollLink2Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LHipRollLink2[0],LHipRoll3[0],LHipRollLink2Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LThigh[0],LHipPitch3[0],LThighPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LThigh[0],LHipPitch3[0],LThighOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LShin[0],LKneePitch3[0],LShinPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LShin[0],LKneePitch3[0],LShinOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LAnklePitchLink[0],LAnklePitch3[0],LAnklePitchLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LAnklePitchLink[0],LAnklePitch3[0],LAnklePitchLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LFoot[0],LAnkleRoll3[0],LFootPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LFoot[0],LAnkleRoll3[0],LFootOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LFootPiece1[0],NAO_LFsrRR[0],LFootPiece1Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LFootPiece1[0],NAO_LFsrRR[0],LFootPiece1Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LFootPiece2[0],NAO_LFsrFR[0],LFootPiece2Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LFootPiece2[0],NAO_LFsrFR[0],LFootPiece2Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LFootPiece3[0],NAO_LFsrRL[0],LFootPiece3Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LFootPiece3[0],NAO_LFsrRL[0],LFootPiece3Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LFootPiece4[0],NAO_LFsrFL[0],LFootPiece4Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LFootPiece4[0],NAO_LFsrFL[0],LFootPiece4Orientation,vrep.simx_opmode_oneshot_wait)
    
        #Right Arm
        vrep.simxSetObjectPosition(clientID,RShoulderPitchLink[0],RShoulderPitch[0],RShoulderPitchLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RShoulderPitchLink[0],RShoulderPitch[0],RShoulderPitchLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RShoulderRollLink[0],RShoulderRoll[0],RShoulderRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RShoulderRollLink[0],RShoulderRoll[0],RShoulderRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RElbowYawLink[0],RElbowYaw[0],RElbowYawLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RElbowYawLink[0],RElbowYaw[0],RElbowYawLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RElbowRollLink[0],RElbowRoll[0],RElbowRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RElbowRollLink[0],RElbowRoll[0],RElbowRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,RWristYawLink[0],RWristYaw[0],RWristYawLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,RWristYawLink[0],RWristYaw[0],RWristYawLinkOrientation,vrep.simx_opmode_oneshot_wait)
    
        #Left Arm
        vrep.simxSetObjectPosition(clientID,LShoulderPitchLink[0],LShoulderPitch[0],LShoulderPitchLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LShoulderPitchLink[0],LShoulderPitch[0],LShoulderPitchLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LShoulderRollLink[0],LShoulderRoll[0],LShoulderRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LShoulderRollLink[0],LShoulderRoll[0],LShoulderRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LElbowYawLink[0],LElbowYaw[0],LElbowYawLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LElbowYawLink[0],LElbowYaw[0],LElbowYawLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LElbowRollLink[0],LElbowRoll[0],LElbowRollLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LElbowRollLink[0],LElbowRoll[0],LElbowRollLinkOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,LWristYawLink[0],LWristYaw[0],LWristYawLinkPosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,LWristYawLink[0],LWristYaw[0],LWristYawLinkOrientation,vrep.simx_opmode_oneshot_wait)
    
        #Left Fingers
        vrep.simxSetObjectPosition(clientID,L_H[0],LWristYawLink[0],NAO_LThumbBasePosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[0],LWristYawLink[0],NAO_LThumbBaseOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[1],L_H[0],Revolute_joint8Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[1],L_H[0],Revolute_joint8Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[2],LWristYawLink[0],NAO_LLFingerBasePosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[2],LWristYawLink[0],NAO_LLFingerBaseOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[3],L_H[2],Revolute_joint12Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[3],L_H[2],Revolute_joint12Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[4],L_H[3],Revolute_joint14Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[4],L_H[3],Revolute_joint14Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[5],LWristYawLink[0],NAO_LRFinger_BasePosition,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[5],LWristYawLink[0],NAO_LRFinger_BaseOrientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[6],L_H[5],Revolute_joint11Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[6],L_H[5],Revolute_joint11Orientation,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectPosition(clientID,L_H[7],L_H[6],Revolute_joint13Position,vrep.simx_opmode_oneshot_wait)
        vrep.simxSetObjectOrientation(clientID,L_H[7],L_H[6],Revolute_joint13Orientation,vrep.simx_opmode_oneshot_wait)
    
    
        vrep.simxSetObjectPosition(clientID,R_H[0],RWristYawLink[0],NAO_RThumbBasePosition,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[0],RWristYawLink[0],NAO_RThumbBaseOrientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[1],R_H[0],Revolute_joint0Position,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[1],R_H[0],Revolute_joint0Orientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[2],RWristYawLink[0],NAO_RLFingerBasePosition,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[2],RWristYawLink[0],NAO_RLFingerBaseOrientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[3],R_H[2],Revolute_joint5Position,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[3],R_H[2],Revolute_joint5Orientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[4],R_H[3],Revolute_joint6Position,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[4],R_H[3],Revolute_joint6Orientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[5],RWristYawLink[0],NAO_RRFinger_BasePosition,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[5],RWristYawLink[0],NAO_RRFinger_BaseOrientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[6],R_H[5],Revolute_joint2Position,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[6],R_H[5],Revolute_joint2Orientation,vrep.simx_opmode_streaming)
        vrep.simxSetObjectPosition(clientID,R_H[7],R_H[6],Revolute_joint3Position,vrep.simx_opmode_streaming)
        vrep.simxSetObjectOrientation(clientID,R_H[7],R_H[6],Revolute_joint3Orientation,vrep.simx_opmode_streaming)


def getStartPosition(clientID):
    #Robo
    Robo=[];
    
    #Head
    HeadYawLink=[];        HeadYaw=[];  HeadPitchLink=[]; HeadPitch=[];
    
    #Left Leg
    LHipYawPitch=[];    LHipRollLink=[];    LHipRoll3=[];   LHipRollLink2=[];   LHipPitch3=[];
    LThigh=[];          LKneePitch3=[];     LShin=[];       LAnklePitch3=[];    LAnklePitchLink=[];
    LAnkleRoll3=[];     LFoot=[];           NAO_LFsrRR=[];  LFootPiece1=[];     NAO_LFsrFR=[];
    LFootPiece2=[];     NAO_LFsrRL=[];      LFootPiece3=[]; NAO_LFsrFL=[];      LFootPiece4=[];
    
    #Right Leg
    RHipYawPitch=[];    RHipRollLink=[];    RHipRoll3=[];   RHipRollLink2=[];   RHipPitch3=[];
    RThigh=[];          RKneePitch3=[];     RShin=[];       RAnklePitch3=[];    RAnklePitchLink=[];
    RAnkleRoll3=[];     RFoot=[];           NAO_RFsrRR=[];  RFootPiece1=[];     NAO_RFsrFR=[];
    RFootPiece2=[];     NAO_RFsrRL=[];      RFootPiece3=[]; NAO_RFsrFL=[];      RFootPiece4=[];

    #Right Arm
    RShoulderPitch=[];  RShoulderPitchLink=[];  RShoulderRoll=[];   RShoulderRollLink=[];   RElbowYaw=[];
    RElbowYawLink=[];   RElbowRoll=[];          RElbowRollLink=[];  RWristYaw=[];           RWristYawLink=[];

    #Left Arm
    LShoulderPitch=[];  LShoulderPitchLink=[];  LShoulderRoll=[];   LShoulderRollLink=[];   LElbowYaw=[];
    LElbowYawLink=[];   LElbowRoll=[];          LElbowRollLink=[];  LWristYaw=[];           LWristYawLink=[];
    
    R_H=[];             L_H=[];             R_Hand=[];      L_Hand=[];


    Body = [HeadYawLink,HeadYaw,HeadPitchLink,HeadPitch,
            LHipYawPitch,LHipRollLink,LHipRoll3,LHipRollLink2,LHipPitch3,LThigh,LKneePitch3,LShin,LAnklePitch3,LAnklePitchLink,
            LAnkleRoll3,LFoot,NAO_LFsrRR,LFootPiece1,NAO_LFsrFR,LFootPiece2,NAO_LFsrRL,LFootPiece3,NAO_LFsrFL,LFootPiece4,
            RHipYawPitch,RHipRollLink,RHipRoll3,RHipRollLink2,RHipPitch3,RThigh,RKneePitch3,RShin,RAnklePitch3,RAnklePitchLink,
            RAnkleRoll3,RFoot,NAO_RFsrRR,RFootPiece1,NAO_RFsrFR,RFootPiece2,NAO_RFsrRL,RFootPiece3,NAO_RFsrFL,RFootPiece4,
            RShoulderPitch,RShoulderPitchLink,RShoulderRoll,RShoulderRollLink,RElbowYaw,RElbowYawLink,RElbowRoll,RElbowRollLink,RWristYaw,RWristYawLink,
            LShoulderPitch,LShoulderPitchLink,LShoulderRoll,LShoulderRollLink,LElbowYaw,LElbowYawLink,LElbowRoll,LElbowRollLink,LWristYaw,LWristYawLink,R_H,R_Hand,L_H, L_Hand]
    
    get_all_handles_start(clientID,Robo, Body)
    
    print 'Body'
    print Body
    
        
    #COLOCA O ROBO NA POSICAO INICIAL
    #Motores Get
    returnCode,JHeadYaw = vrep.simxGetJointPosition(clientID,HeadYaw[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JHeadPitch = vrep.simxGetJointPosition(clientID,HeadPitch[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRHipPitch3 = vrep.simxGetJointPosition(clientID,RHipPitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRHipRoll3 = vrep.simxGetJointPosition(clientID,RHipRoll3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRHipYawPitch = vrep.simxGetJointPosition(clientID,RHipYawPitch[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRKneePitch3 = vrep.simxGetJointPosition(clientID,RKneePitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRAnklePitch3 = vrep.simxGetJointPosition(clientID,RAnklePitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRAnkleRoll3 = vrep.simxGetJointPosition(clientID,RAnkleRoll3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLHipPitch3 = vrep.simxGetJointPosition(clientID,LHipPitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLHipRoll3 = vrep.simxGetJointPosition(clientID,LHipRoll3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLHipYawPitch = vrep.simxGetJointPosition(clientID,LHipYawPitch[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLKneePitch3 = vrep.simxGetJointPosition(clientID,LKneePitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLAnklePitch3 = vrep.simxGetJointPosition(clientID,LAnklePitch3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLAnkleRoll3 = vrep.simxGetJointPosition(clientID,LAnkleRoll3[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRShoulderPitch = vrep.simxGetJointPosition(clientID,RShoulderPitch[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRShoulderRoll = vrep.simxGetJointPosition(clientID,RShoulderRoll[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRElbowRoll = vrep.simxGetJointPosition(clientID,RElbowRoll[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRElbowYaw = vrep.simxGetJointPosition(clientID,RElbowYaw[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JRWristYaw = vrep.simxGetJointPosition(clientID,RWristYaw[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLShoulderPitch = vrep.simxGetJointPosition(clientID,LShoulderPitch[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLShoulderRoll = vrep.simxGetJointPosition(clientID,LShoulderRoll[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLElbowRoll = vrep.simxGetJointPosition(clientID,LElbowRoll[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLElbowYaw = vrep.simxGetJointPosition(clientID,LElbowYaw[0],vrep.simx_opmode_streaming)
    print returnCode
    returnCode,JLWristYaw = vrep.simxGetJointPosition(clientID,LWristYaw[0],vrep.simx_opmode_streaming)
    print returnCode

    #Left Fingers
    returnCode,JNAO_LThumbBase = vrep.simxGetJointPosition(clientID,L_H[0],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint8 = vrep.simxGetJointPosition(clientID,L_H[1],vrep.simx_opmode_streaming)
    returnCode,JNAO_LLFingerBase = vrep.simxGetJointPosition(clientID,L_H[2],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint12 = vrep.simxGetJointPosition(clientID,L_H[3],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint14 = vrep.simxGetJointPosition(clientID,L_H[4],vrep.simx_opmode_streaming)
    returnCode,JNAO_LRFinger_Base = vrep.simxGetJointPosition(clientID,L_H[5],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint11 = vrep.simxGetJointPosition(clientID,L_H[6],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint13 = vrep.simxGetJointPosition(clientID,L_H[7],vrep.simx_opmode_streaming)
    #Right Fingers
    returnCode,JNAO_RThumbBase = vrep.simxGetJointPosition(clientID,R_H[0],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint0 = vrep.simxGetJointPosition(clientID,R_H[1],vrep.simx_opmode_streaming)
    returnCode,JNAO_RLFingerBase = vrep.simxGetJointPosition(clientID,R_H[2],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint5 = vrep.simxGetJointPosition(clientID,R_H[3],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint6 = vrep.simxGetJointPosition(clientID,R_H[4],vrep.simx_opmode_streaming)
    returnCode,JNAO_RRFinger_Base = vrep.simxGetJointPosition(clientID,R_H[5],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint2 = vrep.simxGetJointPosition(clientID,R_H[6],vrep.simx_opmode_streaming)
    returnCode,JRevolute_joint3 = vrep.simxGetJointPosition(clientID,R_H[7],vrep.simx_opmode_streaming)
   

 
    Joints = [JHeadYaw,JHeadPitch,JRHipPitch3,JRHipRoll3,JRHipYawPitch,JRKneePitch3,JRAnklePitch3,JRAnkleRoll3,JLHipPitch3,JLHipRoll3,
              JLHipYawPitch,JLKneePitch3,JLAnklePitch3,JLAnkleRoll3,JRShoulderPitch,JRShoulderRoll,JRElbowRoll,JRElbowYaw,JRWristYaw,JLShoulderPitch,JLShoulderRoll,
              JLElbowRoll,JLElbowYaw,JLWristYaw, JNAO_LThumbBase,JRevolute_joint8,JNAO_LLFingerBase,JRevolute_joint12,JRevolute_joint14,JNAO_LRFinger_Base,JRevolute_joint11,
              JRevolute_joint13, JNAO_RThumbBase,JRevolute_joint0,JNAO_RLFingerBase,JRevolute_joint5,JRevolute_joint6,JNAO_RRFinger_Base,JRevolute_joint2,JRevolute_joint3]

    print 'Joints'
    print Joints

    #Robo
    returnCode,PositionZero =  vrep.simxGetObjectPosition(clientID,Robo[0],-1, vrep.simx_opmode_streaming)
    print returnCode
    returnCode, OrientationZero = vrep.simxGetObjectOrientation(clientID,Robo[0],-1,vrep.simx_opmode_streaming)
    print returnCode
    
    print 'Nao %s %s' % (PositionZero, OrientationZero)

    #Head
    returnCode,HeadYawLinkPosition = vrep.simxGetObjectPosition(clientID,HeadYawLink[0],HeadYaw[0],vrep.simx_opmode_streaming)
    returnCode,HeadYawLinkOrientation = vrep.simxGetObjectOrientation(clientID,HeadYawLink[0],HeadYaw[0],vrep.simx_opmode_streaming)
    returnCode,HeadPitchLinkPosition = vrep.simxGetObjectPosition(clientID,HeadPitchLink[0],HeadPitch[0],vrep.simx_opmode_streaming)
    returnCode,HeadPitchLinkOrientation = vrep.simxGetObjectOrientation(clientID,HeadPitchLink[0],HeadPitch[0],vrep.simx_opmode_streaming)

    Head = [HeadYawLinkPosition, HeadYawLinkOrientation,HeadPitchLinkPosition,HeadPitchLinkOrientation]
    print 'Head'
    print Head 

    #Right Leg
    returnCode,RHipRollLinkPosition = vrep.simxGetObjectPosition(clientID,RHipRollLink[0],RHipYawPitch[0],vrep.simx_opmode_streaming)
    returnCode,RHipRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,RHipRollLink[0],RHipYawPitch[0],vrep.simx_opmode_streaming)
    returnCode,RHipRollLink2Position = vrep.simxGetObjectPosition(clientID,RHipRollLink2[0],RHipRoll3[0],vrep.simx_opmode_streaming)
    returnCode,RHipRollLink2Orientation = vrep.simxGetObjectOrientation(clientID,RHipRollLink2[0],RHipRoll3[0],vrep.simx_opmode_streaming)
    returnCode,RThighPosition = vrep.simxGetObjectPosition(clientID,RThigh[0],RHipPitch3[0],vrep.simx_opmode_streaming)
    returnCode,RThighOrientation = vrep.simxGetObjectOrientation(clientID,RThigh[0],RHipPitch3[0],vrep.simx_opmode_streaming)
    returnCode,RShinPosition = vrep.simxGetObjectPosition(clientID,RShin[0],RKneePitch3[0],vrep.simx_opmode_streaming)
    returnCode,RShinOrientation = vrep.simxGetObjectOrientation(clientID,RShin[0],RKneePitch3[0],vrep.simx_opmode_streaming)
    returnCode,RAnklePitchLinkPosition = vrep.simxGetObjectPosition(clientID,RAnklePitchLink[0],RAnklePitch3[0],vrep.simx_opmode_streaming)
    returnCode,RAnklePitchLinkOrientation = vrep.simxGetObjectOrientation(clientID,RAnklePitchLink[0],RAnklePitch3[0],vrep.simx_opmode_streaming)
    returnCode,RFootPosition = vrep.simxGetObjectPosition(clientID,RFoot[0],RAnkleRoll3[0],vrep.simx_opmode_streaming)
    returnCode,RFootOrientation = vrep.simxGetObjectOrientation(clientID,RFoot[0],RAnkleRoll3[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece1Position = vrep.simxGetObjectPosition(clientID,RFootPiece1[0],NAO_RFsrRR[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece1Orientation = vrep.simxGetObjectOrientation(clientID,RFootPiece1[0],NAO_RFsrRR[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece2Position = vrep.simxGetObjectPosition(clientID,RFootPiece2[0],NAO_RFsrFR[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece2Orientation = vrep.simxGetObjectOrientation(clientID,RFootPiece2[0],NAO_RFsrFR[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece3Position = vrep.simxGetObjectPosition(clientID,RFootPiece3[0],NAO_RFsrRL[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece3Orientation = vrep.simxGetObjectOrientation(clientID,RFootPiece3[0],NAO_RFsrRL[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece4Position = vrep.simxGetObjectPosition(clientID,RFootPiece4[0],NAO_RFsrFL[0],vrep.simx_opmode_streaming)
    returnCode,RFootPiece4Orientation = vrep.simxGetObjectOrientation(clientID,RFootPiece4[0],NAO_RFsrFL[0],vrep.simx_opmode_streaming)
    
    RightLeg = [RHipRollLinkPosition, RHipRollLinkOrientation, RHipRollLink2Position, RHipRollLink2Orientation,RThighPosition,RThighOrientation,RShinPosition,RShinOrientation,
                RAnklePitchLinkPosition,RAnklePitchLinkOrientation,RFootPosition,RFootOrientation,RFootPiece1Position,RFootPiece1Orientation,RFootPiece2Position,RFootPiece2Orientation,
                RFootPiece3Position,RFootPiece3Orientation,RFootPiece4Position,RFootPiece4Orientation]
    print 'RightLeg'
    print RightLeg
    #Left Leg
    returnCode,LHipRollLinkPosition = vrep.simxGetObjectPosition(clientID,LHipRollLink[0],LHipYawPitch[0],vrep.simx_opmode_streaming)
    returnCode,LHipRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,LHipRollLink[0],LHipYawPitch[0],vrep.simx_opmode_streaming)
    returnCode,LHipRollLink2Position = vrep.simxGetObjectPosition(clientID,LHipRollLink2[0],LHipRoll3[0],vrep.simx_opmode_streaming)
    returnCode,LHipRollLink2Orientation = vrep.simxGetObjectOrientation(clientID,LHipRollLink2[0],LHipRoll3[0],vrep.simx_opmode_streaming)
    returnCode,LThighPosition = vrep.simxGetObjectPosition(clientID,LThigh[0],LHipPitch3[0],vrep.simx_opmode_streaming)
    returnCode,LThighOrientation = vrep.simxGetObjectOrientation(clientID,LThigh[0],LHipPitch3[0],vrep.simx_opmode_streaming)
    returnCode,LShinPosition = vrep.simxGetObjectPosition(clientID,LShin[0],LKneePitch3[0],vrep.simx_opmode_streaming)
    returnCode,LShinOrientation = vrep.simxGetObjectOrientation(clientID,LShin[0],LKneePitch3[0],vrep.simx_opmode_streaming)
    returnCode,LAnklePitchLinkPosition = vrep.simxGetObjectPosition(clientID,LAnklePitchLink[0],LAnklePitch3[0],vrep.simx_opmode_streaming)
    returnCode,LAnklePitchLinkOrientation = vrep.simxGetObjectOrientation(clientID,LAnklePitchLink[0],LAnklePitch3[0],vrep.simx_opmode_streaming)
    returnCode,LFootPosition = vrep.simxGetObjectPosition(clientID,LFoot[0],LAnkleRoll3[0],vrep.simx_opmode_streaming)
    returnCode,LFootOrientation = vrep.simxGetObjectOrientation(clientID,LFoot[0],LAnkleRoll3[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece1Position = vrep.simxGetObjectPosition(clientID,LFootPiece1[0],NAO_LFsrRR[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece1Orientation = vrep.simxGetObjectOrientation(clientID,LFootPiece1[0],NAO_LFsrRR[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece2Position = vrep.simxGetObjectPosition(clientID,LFootPiece2[0],NAO_LFsrFR[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece2Orientation = vrep.simxGetObjectOrientation(clientID,LFootPiece2[0],NAO_LFsrFR[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece3Position = vrep.simxGetObjectPosition(clientID,LFootPiece3[0],NAO_LFsrRL[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece3Orientation = vrep.simxGetObjectOrientation(clientID,LFootPiece3[0],NAO_LFsrRL[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece4Position = vrep.simxGetObjectPosition(clientID,LFootPiece4[0],NAO_LFsrFL[0],vrep.simx_opmode_streaming)
    returnCode,LFootPiece4Orientation = vrep.simxGetObjectOrientation(clientID,LFootPiece4[0],NAO_LFsrFL[0],vrep.simx_opmode_streaming)

    LeftLeg = [LHipRollLinkPosition, LHipRollLinkOrientation, LHipRollLink2Position, LHipRollLink2Orientation,LThighPosition,LThighOrientation,LShinPosition,LShinOrientation,
                LAnklePitchLinkPosition,LAnklePitchLinkOrientation,LFootPosition,LFootOrientation,LFootPiece1Position,LFootPiece1Orientation,LFootPiece2Position,LFootPiece2Orientation,
                LFootPiece3Position,LFootPiece3Orientation,LFootPiece4Position,LFootPiece4Orientation]

    print 'LeftLeg'
    print LeftLeg
    #Right Arm
    returnCode,RShoulderPitchLinkPosition = vrep.simxGetObjectPosition(clientID,RShoulderPitchLink[0],RShoulderPitch[0],vrep.simx_opmode_streaming)
    returnCode,RShoulderPitchLinkOrientation = vrep.simxGetObjectOrientation(clientID,RShoulderPitchLink[0],RShoulderPitch[0],vrep.simx_opmode_streaming)
    returnCode,RShoulderRollLinkPosition = vrep.simxGetObjectPosition(clientID,RShoulderRollLink[0],RShoulderRoll[0],vrep.simx_opmode_streaming)
    returnCode,RShoulderRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,RShoulderRollLink[0],RShoulderRoll[0],vrep.simx_opmode_streaming)
    returnCode,RElbowYawLinkPosition = vrep.simxGetObjectPosition(clientID,RElbowYawLink[0],RElbowYaw[0],vrep.simx_opmode_streaming)
    returnCode,RElbowYawLinkOrientation = vrep.simxGetObjectOrientation(clientID,RElbowYawLink[0],RElbowYaw[0],vrep.simx_opmode_streaming)
    returnCode,RElbowRollLinkPosition = vrep.simxGetObjectPosition(clientID,RElbowRollLink[0],RElbowRoll[0],vrep.simx_opmode_streaming)
    returnCode,RElbowRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,RElbowRollLink[0],RElbowRoll[0],vrep.simx_opmode_streaming)
    returnCode,RWristYawLinkPosition = vrep.simxGetObjectPosition(clientID,RWristYawLink[0],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,RWristYawLinkOrientation = vrep.simxGetObjectOrientation(clientID,RWristYawLink[0],RWristYaw[0],vrep.simx_opmode_streaming)
    
    RightArm = [RShoulderPitchLinkPosition,RShoulderPitchLinkOrientation,RShoulderRollLinkPosition,RShoulderRollLinkOrientation,RElbowYawLinkPosition,RElbowYawLinkOrientation,
                RElbowRollLinkPosition,RElbowRollLinkOrientation,RWristYawLinkPosition,RWristYawLinkOrientation]

    print 'RightArm'
    print RightArm
    #Left Arm
    returnCode,LShoulderPitchLinkPosition = vrep.simxGetObjectPosition(clientID,LShoulderPitchLink[0],LShoulderPitch[0],vrep.simx_opmode_streaming)
    returnCode,LShoulderPitchLinkOrientation = vrep.simxGetObjectOrientation(clientID,LShoulderPitchLink[0],LShoulderPitch[0],vrep.simx_opmode_streaming)
    returnCode,LShoulderRollLinkPosition = vrep.simxGetObjectPosition(clientID,LShoulderRollLink[0],LShoulderRoll[0],vrep.simx_opmode_streaming)
    returnCode,LShoulderRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,LShoulderRollLink[0],LShoulderRoll[0],vrep.simx_opmode_streaming)
    returnCode,LElbowYawLinkPosition = vrep.simxGetObjectPosition(clientID,LElbowYawLink[0],LElbowYaw[0],vrep.simx_opmode_streaming)
    returnCode,LElbowYawLinkOrientation = vrep.simxGetObjectOrientation(clientID,LElbowYawLink[0],LElbowYaw[0],vrep.simx_opmode_streaming)
    returnCode,LElbowRollLinkPosition = vrep.simxGetObjectPosition(clientID,LElbowRollLink[0],LElbowRoll[0],vrep.simx_opmode_streaming)
    returnCode,LElbowRollLinkOrientation = vrep.simxGetObjectOrientation(clientID,LElbowRollLink[0],LElbowRoll[0],vrep.simx_opmode_streaming)
    returnCode,LWristYawLinkPosition = vrep.simxGetObjectPosition(clientID,LWristYawLink[0],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,LWristYawLinkOrientation =vrep.simxGetObjectOrientation(clientID,LWristYawLink[0],LWristYaw[0],vrep.simx_opmode_streaming)

    LeftArm = [LShoulderPitchLinkPosition,LShoulderPitchLinkOrientation,LShoulderRollLinkPosition,LShoulderRollLinkOrientation,LElbowYawLinkPosition,LElbowYawLinkOrientation,
                LElbowRollLinkPosition,LElbowRollLinkOrientation,LWristYawLinkPosition,LWristYawLinkOrientation]

    print 'LeftArm'
    print LeftArm

    #Left Fingers
    returnCode,NAO_LThumbBasePosition = vrep.simxGetObjectPosition(clientID,L_H[0],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_LThumbBaseOrientation = vrep.simxGetObjectOrientation(clientID,L_H[0],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint8Position = vrep.simxGetObjectPosition(clientID,L_H[1],L_H[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint8Orientation = vrep.simxGetObjectOrientation(clientID,L_H[1],L_H[0],vrep.simx_opmode_streaming)
    returnCode,NAO_LLFingerBasePosition = vrep.simxGetObjectPosition(clientID,L_H[2],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_LLFingerBaseOrientation = vrep.simxGetObjectOrientation(clientID,L_H[2],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint12Position = vrep.simxGetObjectPosition(clientID,L_H[3],L_H[2],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint12Orientation = vrep.simxGetObjectOrientation(clientID,L_H[3],L_H[2],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint14Position = vrep.simxGetObjectPosition(clientID,L_H[4],L_H[3],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint14Orientation = vrep.simxGetObjectOrientation(clientID,L_H[4],L_H[3],vrep.simx_opmode_streaming)
    returnCode,NAO_LRFinger_BasePosition = vrep.simxGetObjectPosition(clientID,L_H[5],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_LRFinger_BaseOrientation = vrep.simxGetObjectOrientation(clientID,L_H[5],LWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint11Position = vrep.simxGetObjectPosition(clientID,L_H[6],L_H[5],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint11Orientation = vrep.simxGetObjectOrientation(clientID,L_H[6],L_H[5],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint13Position = vrep.simxGetObjectPosition(clientID,L_H[7],L_H[6],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint13Orientation = vrep.simxGetObjectOrientation(clientID,L_H[7],L_H[6],vrep.simx_opmode_streaming)

    LeftFingers = [NAO_LThumbBasePosition,NAO_LThumbBaseOrientation,Revolute_joint8Position,Revolute_joint8Orientation,NAO_LLFingerBasePosition,NAO_LLFingerBaseOrientation,
                   Revolute_joint12Position,Revolute_joint12Orientation,Revolute_joint14Position,Revolute_joint14Orientation,NAO_LRFinger_BasePosition,
                   NAO_LRFinger_BaseOrientation, Revolute_joint11Position,Revolute_joint11Orientation,Revolute_joint13Position,Revolute_joint13Orientation]

    print 'LeftFingers'
    print LeftFingers


    returnCode,NAO_RThumbBasePosition = vrep.simxGetObjectPosition(clientID,R_H[0],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_RThumbBaseOrientation = vrep.simxGetObjectOrientation(clientID,R_H[0],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint0Position = vrep.simxGetObjectPosition(clientID,R_H[1],R_H[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint0Orientation = vrep.simxGetObjectOrientation(clientID,R_H[1],R_H[0],vrep.simx_opmode_streaming)
    returnCode,NAO_RLFingerBasePosition = vrep.simxGetObjectPosition(clientID,R_H[2],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_RLFingerBaseOrientation = vrep.simxGetObjectOrientation(clientID,R_H[2],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint5Position = vrep.simxGetObjectPosition(clientID,R_H[3],R_H[2],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint5Orientation = vrep.simxGetObjectOrientation(clientID,R_H[3],R_H[2],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint6Position = vrep.simxGetObjectPosition(clientID,R_H[4],R_H[3],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint6Orientation = vrep.simxGetObjectOrientation(clientID,R_H[4],R_H[3],vrep.simx_opmode_streaming)
    returnCode,NAO_RRFinger_BasePosition = vrep.simxGetObjectPosition(clientID,R_H[5],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,NAO_RRFinger_BaseOrientation = vrep.simxGetObjectOrientation(clientID,R_H[5],RWristYaw[0],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint2Position = vrep.simxGetObjectPosition(clientID,R_H[6],R_H[5],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint2Orientation = vrep.simxGetObjectOrientation(clientID,R_H[6],R_H[5],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint3Position = vrep.simxGetObjectPosition(clientID,R_H[7],R_H[6],vrep.simx_opmode_streaming)
    returnCode,Revolute_joint3Orientation = vrep.simxGetObjectOrientation(clientID,R_H[7],R_H[6],vrep.simx_opmode_streaming)

    RightFingers = [NAO_RThumbBasePosition,NAO_RThumbBaseOrientation,Revolute_joint8Position,Revolute_joint8Orientation,NAO_RLFingerBasePosition,NAO_RLFingerBaseOrientation,
                   Revolute_joint12Position,Revolute_joint12Orientation,Revolute_joint14Position,Revolute_joint14Orientation,NAO_RRFinger_BasePosition,
                   NAO_RRFinger_BaseOrientation, Revolute_joint11Position,Revolute_joint11Orientation,Revolute_joint13Position,Revolute_joint13Orientation]

    print 'RightFingers'
    print RightFingers

    return PositionZero, OrientationZero
