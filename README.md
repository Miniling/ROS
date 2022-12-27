# ROS

ROS based autonomous driving 🚗 <br>
ros needs linux OS. <br>
Use VM or Ubuntu(dual booting). <br>
This study is ran from ubuntu 18.04.2
 <br> <br>
 
<h2>ROS(Robot Operating System)</h2>
 - 운영체제 위에 한 단계 더 올라가서 작업하는 '메타 운영체제' <br>
 - 모든 로봇을 제어할 수 있는 다양한 기능의 프레임워크를 지원하지는 않지만, 약간의 모듈을 추가하여 편리하게 코드를 재사용할 수 있음. <br>
 - 디버깅 및 시각화, 시뮬레이션 등의 다양한 도구를 통해 개발의 속도를 향상. <br>
 - Ubuntu에서 Python과 C++을 기반으로, 프로세스(노드) 사이의 통신 가능. <br>
 - 여러 프로세스 사이의 통신 부분을 담당하는 중간 다리 역할.
<br>

<h2>ROS Filesystem</h2>
 - Meta Package: 특수화된 패키지로서, 관련된 패키지들을 모아놓은 것. <br>

ROS Master: Parameter Server, Topic 및 Service, Message, Node에 대한 관리. <br>
Node: 기본 프로세스. <br>
Message: 송수신 데이터. <br>
Bags: ROS에서 데이터를 저장 및 불러올 때 사용, Master에서 확인 가능한 Topic들을 모두 저장 가능, 이를 다시 재생하는 기능 제공. <br>
Topics: 메시지를 식별하기 이름을 붙여놓은 것. Topic을 보내는 것을 Publish, 받는 것을 Subscribe, 기록하는 것을 Bags.
<br>

<h2>ROS 명령어</h2>
 '명령어' + '패키지' + '파일' 순으로 입력. <br>
 (
 - roscore: ROS master 실행. <br>
 - roscd: 위치한 ros 패키지의 폴더로 이동. <br>
 - rosls: <br>
 - rosed: <br>
 - roscp: <br>
 - rosd: <br>
 - rosservice: <br>
 - rosnode: <br>
 - roseparam: <br>
 - rosbag: <br>
 - rosmsg: <br>
 - rossov: <br>
 - catkin_create_pkg: 새로운 패키지 생성 <br>
 - catkin_make: catkin 작업 공간의 C++ 파일 빌드 <br>
 - rospack: 파일 시스템에서 사용 가능한 패키지의 정보 검색 <br>
 - rosdep: 시스템 의존성 파일들을 설치 <br>
 - rviz: 3D 시각화를 위한 rviz를 실행 <br>
 - rqt: 데이터 시각화를 위한 rqt를 실행 <br>

