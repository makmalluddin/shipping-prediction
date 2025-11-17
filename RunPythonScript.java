import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RunPythonScript {
    public static void main(String[] args) {
        try {
            // Command to run the Python script with arguments
            String[] command = {
                "/home/makmalluddin/Documents/projekstupen/bin/python", 
                "/home/makmalluddin/Documents/projekstupen/Stupen/LastProject/shipcmd.py", 
                "DEBIT", 
                "91.250000",
                "314.640015", 
                "18.251453",
                "-66.037056", 
                "Standard Class",
                "2", 
                "Southeast Asia",
                "Indonesia", 
                "Bandung",
                "Pacific Asia", 
                "Late delivery",
                "31", "1",
                "2018", "3",
                "2", "2018"
            };

            // Start the process
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.redirectErrorStream(true); // Combine standard output and error streams
            Process process = processBuilder.start();

            // Capture the output of the script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for the process to complete and get the exit status
            int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
