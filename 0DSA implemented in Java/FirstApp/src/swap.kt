fun main(){
    println("Enter value of a:")
    var a= readLine()!!.toInt()
    println("Enter value of b:")
    var b= readLine()!!.toInt()
    var c=0
    println("Before Swap :")
    println("A=$a")
    println("B=$b")

    c=a
    a=b
    b=c

    println("After Swap :")
    println("A=$a")
    println("B=$b")

}
//with two variable :
//var x=10
//
//var y=20
//
//x = x+y
//
//y = x-y
//
//x = x-y