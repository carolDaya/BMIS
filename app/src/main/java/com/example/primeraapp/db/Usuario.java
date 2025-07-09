package com.example.primeraapp.db;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "usuarios")
public class Usuario {
    @PrimaryKey
    public int id;
    public String nombre;
    public String telefono;
    public String password;
    public String rol;
    public String estado;
    public boolean conectado;
    public String ultima_conexion;
}
