package com.example.primeraapp.db;

import androidx.room.Dao;
import androidx.room.Query;

@Dao
public interface UsuarioDao {
    @Query("SELECT * FROM usuarios WHERE telefono = :telefono AND password = :password LIMIT 1")
    Usuario login(String telefono, String password);
}