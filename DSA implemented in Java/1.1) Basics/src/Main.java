class Student{
    String stuName;
    int stuId;
    String stuCity;

    public void studentDetails(){
        System.out.println("Student name is "+ stuName);
        System.out.println("Student enrolment no. is "+ stuId);
        System.out.println("Student city is "+ stuCity);
    }
}


public class Main {
    public static void main(String[] args) {
        // Creating object of class

        Student st1 = new Student();
        st1.stuName = "Shaan";
        st1.stuId = 10;
        st1.stuCity = "Kodinar";

        st1.studentDetails();
    }
}