// console.log("start")

// setTimeout(() => {
//     console.log("Hello1")
//     setTimeout(() => {
//         console.log("hello2")
//     }, 0)
// }, 0)

// setTimeout(() => {console.log("3")}, 0)
// let hh = ["hSDFasde", "sssdsd", "jjjjjj", "hhhhhh", "1", 2, 3 ,4]
// let numberss = [1, 2, 45, 23, 222]
// for(let i = 0; i < hh.length; i++) {
//     hh[i] = hh[i][0].toUpperCase() + hh[i].slice(1).toLowerCase()
// }
// hh.forEach((item, i, arr) => {
//     arr[i] = item[0].toUpperCase() + item.slice(1).toLowerCase()
// })
// let atLast = hh.map((item) => {
//     return item[0].toUpperCase() + item.slice(1).toLowerCase()
// })
// let filll = hh.filter((item) => typeof item === 'string' && isNaN(item))
// let result = []
// result.push(hh.some((item) => typeof item === "number"))
// numberss.reduceRight((acc, item) => {
//     console.table({acc, item})
//     return acc + item
// }, 0)
// const hhhyyp = new XMLHttpRequest();
// hhhyyp.onreadystatechange = function(){
//     if(this.readyState == 4 && status == 200){
//         myFunction(this.responseText)
//     }
// }
// hhhyyp.setRequestHeader("Content-type", " application/x-www-form-urlencoded")

// hhhyyp.open("POST", "http://getpost.itgid.info/index2.php", true)
// hhhyyp.send("ключ")

// function myFunction(data){
//     console.log(data)
// }
let ageOne = "12"
let ageOld = 13
let ressult = (ageOld == ageOne) ? "Правльно" : 
(ageOne > ageOne) ? "Интересно" : 
(ageOne < ageOld) ? "Действительно интересно" : "Какая интересная ситуация"
console.log(ressult)

let user = {
    name: "John",
    money: 1000,
  
    [Symbol.toPrimitive](hint) {
      alert(`hint: ${hint}`);
      return hint == "string" ? `{name: "${this.name}"}` : this.money;
    }
  }
  console.log((0.1 + 0.2).toFixed())
  // демонстрация результатов преобразований:
  alert(user); // hint: string -> {name: "John"}
  alert(+user); // hint: number -> 1000
  alert(user + 500); // hint: default -> 1500

  