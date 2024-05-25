fun main()
{
    println("Enter your age : ")
    var age= readLine()!!.toInt()
    if (age>18) {
        println("Age is Greater than 18.")
        println("Age : $age")
    }
    if (age in 20 .. 25) {
        println("Age : $age")
    }
    else if (age<18) {
        println("Age is less than 18.")
        println("Age : $age")
    }

    else
        println("Age : $age")
       print("Bhag , chutiye itna bhi nahi pata.")
}