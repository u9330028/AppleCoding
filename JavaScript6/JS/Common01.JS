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


//object도 복사 해서 사용해서 가능 합니다.
//01.중복은 뒷 값을 적용이 가능 합니다.
var o1 = { a: 1, b: 2 };
var o2 = { ...o1, c: 3 };

console.log(o2);

//...은 중괄호/소괄호/함수 안에서 사용 가능 합니다.



//*********************************************************** */

//함수에 파라메터를 넣을때 사용 합니다.
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
