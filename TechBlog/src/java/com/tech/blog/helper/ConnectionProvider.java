package com.tech.blog.helper;

import java.sql.*;

public class ConnectionProvider {

    public static Connection con;

    public static Connection getConnection() {
        
        try {
            
            if (con == null) {
                
                 Class.forName("com.mysql.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/techblog","root","");
                
            }
            
        } catch (Exception e) {
           
            e.printStackTrace();
        }
    return con;
    }
}
