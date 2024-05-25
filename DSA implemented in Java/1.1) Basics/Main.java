class Student{
    String stuName;
    int stuId;
    String stuCity;

    public Student(){
        System.out.println("Creating constructor - Nom-parameterized Constructor"); // Nom-parameterized Constructor
    }

    public Student(int i, String n, String c){
        System.out.println("Creating constructor - parameterized Constructor");
        stuId = i;
        stuName = n;
        stuCity = c;
    }

    public void studentDetails(){
        System.out.println("Student name is "+ stuName);
        System.out.println("Student enrolment no. is "+ stuId);
        System.out.println("Student city is "+ stuCity);
    }
}

public class Constructor {
    public static void main(String[] args) {
        // Creating object of class

        Student st1 = new Student();
        st1.stuName = "Shaan";
        st1.stuId = 10;
        st1.stuCity = "Kodinar";

        st1.studentDetails();

        Student st2 = new Student(11, "Shalu", "Veraval");
        st2.studentDetails();
    }
}

//OUTPUT
/*
Creating constructor - Nom-parameterized Constructor
Student name is Shaan
Student enrolment no. is 10
Student city is Kodinar
Creating constructor - parameterized Constructor
Student name is Shalu
Student enrolment no. is 11
Student city is Veraval
*/