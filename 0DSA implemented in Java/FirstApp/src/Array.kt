fun main(){
    var maxSize=5
    var listOfPets:Array<String> = Array(size = maxSize){""}
    for (i in 0..4){
        listOfPets[i]= readLine()!!.toString()
    }

    for (i in 0..4){
        println("Pets : $i = ${listOfPets[i]}")
    }
    //listOfPets[0]= readLine()!!.toString()
    //listOfPets[1]= readLine()!!.toString()
    //listOfPets[2]= readLine()!!.toString()
}