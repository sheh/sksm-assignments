import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class DateExample {
    public static void main(String[] args) {
        // Old java date time parsing was used so potentially wrong date could be parsed 
        // without exception and date object was mutable and not thread safe.
        DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String dateString = "2024-05-13 14:30:00";
        try {
            LocalDateTime date = LocalDateTime.parse(dateString, FORMATTER);
            System.out.println("Date: " + date);
        } catch (DateTimeParseException e) {
            e.printStackTrace();
        }
    }
}