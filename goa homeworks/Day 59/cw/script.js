let num = Number(prompt("enter num:"));
let numb = Number(prompt("enter num:"));

let sum = num + numb;
console.log( sum);


let name1 = prompt(" enter Your name:");
console.log("hello, " , name1 , "!");

submit.addEventListener("click",function(event) {
    event.preventDefault()
    let nameinput=document.getElementsByName("name").value
    console.log("User name:", nameinput)
})