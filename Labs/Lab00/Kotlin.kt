fun main() {
    // Lab 00 but with Kotlin
    println("Hello! Welcome to Lab 00 for Programming Foundations 1!")
    println("Please record your attendance by entering your name, student ID, UI e-mail, and hobby down below.")

    print("Name : ")
    var name = readLine()
    print("Student ID : ")
    var studentId = readLine()
    print("UI E-mail : ")
    var email = readLine()
    print("Hobby : ")
    var hobby = readLine()
    println("")

    println("Please write one word that describes programming for you!")
    var answer = readLine()

    println("Attendance recorded for student $name with student ID $studentId with UI e-mail $email and hobby of $hobby")
    println("Thank you for coming to today's lab session. See you next week!")
}