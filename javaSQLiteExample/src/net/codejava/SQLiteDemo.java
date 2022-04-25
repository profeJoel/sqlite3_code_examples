package net.codejava;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SQLiteDemo {
    public static void main(String[] args){
        String jdbcUrl = "jdbc:sqlite:/C:\\Users\\joelm\\Desktop\\respaldo\\codigos\\sqlite3_code_examples\\javaSQLiteExample\\usersdb.db";
        try{
            Connection connection = DriverManager.getConnection(jdbcUrl);
            //String sql = "SELECT * FROM users";
            String sql = "SELECT rowid, * FROM users";
            Statement statement = connection.createStatement();
            ResultSet result = statement.executeQuery(sql);

            while(result.next()){
                Integer id = result.getInt("rowid");
                String name = result.getString("name");
                String email = result.getString("email");

                System.out.println(id + "|" + name + "|" + email);
            }
        }catch(SQLException e){
            System.out.println("Error connection to SQLite database");
            e.printStackTrace();
        }
    }
}
