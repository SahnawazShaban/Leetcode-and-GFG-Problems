fun main(){
    val msg1="Welcome to Switzerland "
    val msg2="Sahnawaz Shaban"
    val allmsg=msg1+msg2
    println(allmsg.toLowerCase())
    println(allmsg.toUpperCase())
    println(allmsg.trim())

    val listoftoken=allmsg.trim().split("")
    for (token in listoftoken)
    {
        if(!token.contains("to") && !token.contains("is"))
        {
            print("token : $token")
        }
    }
}