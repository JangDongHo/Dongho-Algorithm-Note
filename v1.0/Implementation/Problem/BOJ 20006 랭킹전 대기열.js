// https://www.acmicpc.net/problem/20006

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
const input = fs.readFileSync(filePath).toString().trim().split('\n');

// 1. 입력 처리
const [p, m] = input[0].split(" ").map(Number);

// 2. players 배열 생성
const players = input.slice(1).map(line => {
  const [level, nickname] = line.split(" ");
  return { level: +level, nickname };
});

// 3. Room 클래스 정의
class Room {
  constructor(level, roomSize) {
    this.players = [];
    this.min_level = level - 10;
    this.max_level = level + 10;
    this.roomSize = roomSize;
  }

  canEnter(level) {
    return this.players.length < this.roomSize && level >= this.min_level && level <= this.max_level;
  }

  addPlayer(level, nickname) {
    this.players.push({ level, nickname });
  }

  isFull() {
    return this.players.length === this.roomSize;
  }

  getPlayersSortedByNickname() {
    return this.players.slice().sort((a, b) => a.nickname.localeCompare(b.nickname));
  }

  getStatus() {
    return this.isFull() ? 'Started!' : 'Waiting!';
  }
}

// 4. 플레이어를 방에 매칭하는 함수
function matchPlayersToRooms(players, roomSize) {
  const rooms = [];

  for (let { level, nickname } of players) {
    let entered = false;

    for (let room of rooms) {
      if (room.canEnter(level)) {
        room.addPlayer(level, nickname);
        entered = true;
        break;
      }
    }

    if (!entered) {
      const newRoom = new Room(level, roomSize);
      newRoom.addPlayer(level, nickname);
      rooms.push(newRoom);
    }
  }

  return rooms;
}

// 5. 매칭 실행
const rooms = matchPlayersToRooms(players, m);

// 6. 결과 출력
for (let room of rooms) {
  console.log(room.getStatus());

  for (let { level, nickname } of room.getPlayersSortedByNickname()) {
    console.log(`${level} ${nickname}`);
  }
}
