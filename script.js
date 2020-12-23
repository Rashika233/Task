let arr = [1,2, true,false, {}, '', 5,6 ]
for (let i = 0; i < arr.length; i++) {
    if (arr[i] != true) {
        result = false;
        break;
    }
}
console.log(result);



var array = [1,2, true,false, {}, '', 5,6 ]
var index=0;
array.forEach(check);
function check(value,index){
 if(value==true)
 array[index]=true;
 else
 array[index]=false;
}
console.log(array);