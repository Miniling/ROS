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
 꿀팁! 'Tab'키를 사용하면 명령어를 확인 및 사용할 수 있다! <br><br>
 - roscore: ROS master 실행. <br>
 - rosrun: 파일(노드) 실행. <br>
 - roslaunch: 파일(노드) 여러개 실행. <br>
 - rosclean: ROS 로그 파일 검사 및 삭제. <br>
 - rostopic: topic 관련 명령어. <br>
  -- echo: topic 출력(퍼블리셔가 전달하는 토픽(메세지) 출력). <br>
  -- find: topic 찾기 <br>
  -- info: topic 정보(상세) <br>
  -- list: topic 목록 <br>
  -- pub: publishing. 전달할 토픽(메세지) 직접 입력 가능. (option -r: rate(퍼블리싱 속도)) 
 - roscd: 위치한 ros 패키지의 폴더로 이동 <br>
 - rosls: ros 패키지 파일 목록 <br>
 - rosed: ros 패키지 파일 편집 <br>
 - roscp: ros 패키지 파일 복사 <br>
 - rospd: ros 디렉터리 인덱스에 디렉터리 추가 <br>
 - rosd: ros 디렉터리 인덱스 확인 <br>
 - rosservice: ros 서비스 정보 확인 <br>
 - rosnode: ros 노드 정보 확인 <br>
 - roseparam: ros 파라미터 정보 확인 <br>
 - rosbag: ros 기록(==리눅스 history) 및 재생(linux'history와의 차이점) <br>
 - rosmsg: ros 메시지 정보 확인 <br>
 - rossrv: ros 서비스 정보 확인 <br>
 - rosversion: ros 패키지 및 배포 릴리즈 버전 정보 확인 <br>
 - roswtf: ros 시스템 검사 <br>
 - catkin_create_pkg: 새로운 패키지 생성 <br>
 - catkin_make: 캐킨 작업 공간의 C++ 파일 빌드 <br>
 - catkin_eclipse: 캐킨 빌드 시스템으로 생성한 패키지를 이클립스에서 사용할 수 있게 변경 <br>
 - catkin_prepare_release: 릴리즈 할 때 사용되는 로그 정리 및 버전 태깅 <br>
 - catkin_generate_changelog: 릴리즈 할 때 CHANGELOG.rst 파일 생성 또는 업데이트 <br>
 - catkin_init_workspace: 캐킨 빌드 시스템의 작업 폴더 초기화 <br>
 - catkin_find: 캐킨 검색 <br>
 - rospack: 파일 시스템에서 사용 가능한 패키지의 정보 검색 <br>
 - rosinstall: ros 추가 패키지 설치 <br>
 - rosdep: 시스템 의존성 파일들을 설치 <br>
 - roslocate: ros 패키지 정보 관련 명령어 <br>
 - roscreate-pkg: ros 패키지 자동 생성 <br>
 - rosmake: ros 패키지 빌드 <br>
 - rviz: 3D 시각화를 위한 rviz를 실행 <br>
 - rqt: 데이터 시각화를 위한 rqt를 실행 <br>
<br>

인지 -> 판단 -> 제어 <br>
sensor algorithm motor<br>
<br>

<h3>※주의!!!</h3>
리눅스 기반이기 때문에 절대적으로 영문만! 사용!<br>
파이썬 파일에 주석을 작성하더라도 무조건! 영문으로만! 작성!<br>
<br>

<h2>자동차 주행 방법</h2>
<a>1.애커만</a>
<a>2.디퍼</a>
<a>3.옴니</a>


<h2>OpenCV</h2>
영상처리 <br>
카메라로 받아온 데이터에서 도로 영역만을 확인하여, 차선 및 도로방향지시 추출 <br>
추출한 데이터를 바탕으로 차선기반 주행 <br>
 - 검출된 차선 주행 <br>
 - 계산된 차선과의 거리값과 각도를 이용하여 제어 <br>
 - 위에서 구한 곡률로부터 steering값을 계산 <br>
 - pure persuit에서 사용하는 식을 통해 계산, 뒷축을 기준으로 한 점에 대하여 곡률을 구한 다음 steering값을 구하여 그 차량의 점을 추종하는 방식. <br>
 - k는 곡률, L은 차량의 길이, delta는 조향각을 의미.  k=1/R, R=L/tan(delta) <br>
 - 조향각 delta를 구하기 위해 위의 식을 아래 식에 대입하면 1/k=L/tan(delta) 식을 얻을 수 있음. <br>
 - 카메라를 통해서 Local path를 계산할 수 있음. <br>
 <br>
 
 <h2>SLAM</h2>
 - Simultaneous Localization And Mapping, 동시적 위치 추정 및 지도 작성) <br>
  - auto driving: 특정 조건을 만족하면서 주행(ex: 차선인식 등) <br>
  - navigation: map상에서 출발지 및 목적지에 따라 경로를 생성하고 자율로 주행 <br>
 <p>Bayesian Theory</p>
  - 처음 위치는 알 수 없지만, 다음에 오는 정보에서 위치를 예측(특징점 활용) <br>
 <p>Motion model</p>
  - 실제 로봇에는 odometry-based model과 velocity-based model로 구분 <br>
  - 현재는 제어기의 성능 향상으로 두 가지 모두를 이용해 위치를 추정 <br>
