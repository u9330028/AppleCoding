var arrT = ['hello', 'world'];
console.log(arrT);
console.log(...arrT);

//spread operator
var arrA = 'hello';
console.log(...arrA);


let a = [1, 2, 3, 5];
let b = [5, 6];

let c = [...a, ...b];

console.log(c);

//Deep copy -> ...a
//reference type


//object�� ���� �ؼ� ����ؼ� ���� �մϴ�.
//01.�ߺ��� �� ���� ������ ���� �մϴ�.
var o1 = { a: 1, b: 2 };
var o2 = { ...o1, c: 3 };

console.log(o2);

//...�� �߰�ȣ/�Ұ�ȣ/�Լ� �ȿ��� ��� ���� �մϴ�.



//*********************************************************** */

//�Լ��� �Ķ���͸� ������ ��� �մϴ�.
let add = (a, b, c) => { console.log(a + b + c) }

add(...a);
//add(...b);


//call, appy
var nn = 'GiJin';
let ps = {
    A: () => { console.log(this.name + '  bye') },
    B: () => { console.log("good game") }
}

let ps2 = {
    name: 'AGAA'
}
ps.A.apply(ps2);
ps.B();


//function upgrade..
let Add = () => { return 20 }
let Sum = (a, b = 10) => { console.log(a + b) }

Sum(2);
Sum(2, Add);

function ArgU0(a, b, c) {
    console.log(arguments[0])
    console.log(arguments[1])
    console.log(arguments[2])
}
//argument (parameter) return
function ArgU1(a, b, c) {
    for (var i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}

let ArgU2 = (a, b, c) => {
    console.log(`a = ${a} b = ${b} c = ${c}`);
}

let ArgU3 = (...rest) => {
    console.log(`a = ${rest[0]} b = ${rest[1]} c = ${rest[2]}`);
}

let ArgU4 = (a, ...rest) => {
    console.log("a ==> " + a + ` a = ${rest[0]} b = ${rest[1]} c = ${rest[2]}`);
}

ArgU0(1, 2, 3);
ArgU1(3, 4, 5);
ArgU2(3, 4, 5);
ArgU4("A", 4, 5, 6);

//=-=================================================================
//Question 1
var aa = [1, 2, 3];
var bb = '김밥';
var cc = [...bb, ...aa];
console.log(cc);


//Question 2
a = [1, 2, 3];
b = ['you', 'are'];
c = function (a, b) {
    console.log([[...a], ...[...b]][0])
}
c(a, b); //-> [[1,2,3],you, are]


//Question 3
function 함수(a = 5, b = a * 2) {
    console.log(a + b);
    return 10
}
함수(4); //-> 12

//Question 4
function 함수(a = 5, b = a * 2) {
    console.log(a + b);
}
함수(undefined, undefined); //15

//Question 5
function 어레이(...newArray) {
    return [...newArray];
}

var newArray = 어레이(1, 2, 3, 4, 5);
console.log(newArray);

//Question 6
var numbers = [2, 3, 4, 5, 6, 1, 3, 2, 5, 5, 4, 6, 7];
console.log(Math.max(...numbers));


//Question 7
function 정렬(arrB) {
    var ii = arrB;
    ii = [...ii];
    // for (var i = 0; i < arrB.length; i++) {
    //     //        ii = arrB[i];
    //     console.log(ii.sort());
    // }
    console.log(ii.sort());
}

정렬('bear');

//Question 8
function JJ(inPut) {
    var inC = inPut;
    var arrC = [...inC];
    var objC = new Object();
    for (var i = 0; i < arrC.length; i++) {
        let wcount = arrC.filter(element => arrC[i] === element).length;
        console.log(wcount);

        objC[arrC[i]] = wcount;

    }

    console.log(objC);
}


var NN = { name: 'Jane' };


//새로 변수를 만드는 것과 동일하다.
function KK(obj) {
    obj = { name: 'Kim' };
    var objR = obj;
    console.log(`${NN.name} __ ${objR.name}`);
}


JJ('aaacccabcef');

KK(NN);


//부가세

var DD = {
    product: 'hey',
    price: 2000,
    tax: function () {
        console.log(`부가세는 ${this.price * 0.1} 입니다`);
    }
}


function Pd(Nn, Pr) {
    this.product = Nn,
        this.Price = Pr,
        this.Tax = function () {
            console.log(`부가세는 ${this.Price * 0.1} 입니다`);
            //console.log(this.Price * 0.1);
        }
}

Pd.prototype.func = function () {
    console.log("Prototype 테스트 중 입니다.");
}

var AAA = new Pd('감자', 1000);
var BBB = new Pd('호박', 3000);
BBB.func();

var arrA = ['a', 'b', 'c'];
var arrD = new Array(1, 2, 3);

console.log(Array.prototype);


function MM() {
    this.name = 'kim';
    this.age = 15;
}

MM.prototype.gender = '남';

var mm = new MM();


function student(name, age) {
    this.name = name;
    this.age = age;
    this.sayhi = function () {
        console.log("hi myname " + this.name + "oo");
    }

}

var stu1 = new student('kim', 30);
stu1.sayhi();

function Parent() {
    this.name = 'kim';
}

var ccc = new Parent();
ccc.__proto__.name = 'park';
console.log(ccc.name);


Array.prototype.del3 = function () {
    for (var i = 0; i < this.length; i++) {
        if (this[i] === 3) {
            this.splice(i, 1);
        }
    }
};

var arrT = [1, 2, 3, 4];
arrT.del3();

console.log(arrT);


var aTT = { name: 'kk', age: 30 };
var aTTh = Object.create(aTT);

aTTh.age = 40;

var aTThh = Object.create(aTTh);


class ParentAll {
    constructor() {
        this.brother1 = 'can';
        this.brother2 = 'do';
    }

    get getbrothers() {
        return this.brother1 + " " + this.brother2;
    }

    set setbrother1(nn) {
        this.brother1 = String(nn);
    }
}


class ParentAll2 extends ParentAll {
    constructor() {
        super()
        this.brother3 = 'it';
    }

    fnCall() {
        console.log(this.brother1 + this.brother2 + this.brother3);
    }
}

var pA = new ParentAll2();
pA.fnCall();

class 강아지 {
    constructor(C, T) {
        this.type = T;
        this.color = C;
    }

    //     toGo(this instanceof 개) {
    //     this.age++;
    // }
}

var 강아지1 = new 강아지('말티즈', '흰색');
var 강아지2 = new 강아지('진돗개', '브랙');

class 개 extends 강아지 {
    constructor(C, T, D) {
        super(C, T);
        this.age = D;
    }
}

var 강아지3 = new 개("a", 'B', 3);

var data = {
    odd: [1, 3],
    even: [2, 4, 6],
    get getter함수() {
        return [...this.odd, ...this.even].sort()
    }
};

console.log(data.getter함수);


//*Part-03//////////////////////////////////////////////////////////////////
//틀린그림 찾기능력이 향상되는 Destructuring 문법

var [x, y, z] = [1, 2, 3];

var { xx, yy } = { xx: 'a', yy: 'b' };

xx = 'b';
yy = 'c';

var zz = { xx: xx, yy: yy };
zz = { xx, yy };

function zzz([a, b]) {
    console.log(a);
    console.log(b);
}

zzz([1, 2]);

