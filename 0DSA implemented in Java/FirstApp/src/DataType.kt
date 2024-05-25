fun main(){
    val name="Sahnawaz"
    val age=20
    val CGPA=9.26

    println("======User Information=======")
    println("Name : "+name)
    println("Age: "+ age)
    println("CGPA: "+ CGPA)

    var department:String?
    department=null
    department="Software Engineering"
    println("Department : ${department!!}") // !! - it not should be null
}