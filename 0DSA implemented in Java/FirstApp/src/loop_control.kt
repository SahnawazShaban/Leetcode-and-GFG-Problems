fun main(){
    println("Increment :")
    for (i in 1..15 step 3){
        println("$i : Hey Shaan ")
    }

    println("Decrement :")
    for (i in 15 downTo 0 step 3){
        println("$i : Hey Shaan ")
    }
}