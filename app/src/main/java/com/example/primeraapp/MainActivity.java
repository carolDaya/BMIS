package com.example.primeraapp;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.example.primeraapp.db.AppDatabase;
import com.example.primeraapp.db.Usuario;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); // usa el layout XML

        TextView textView = findViewById(R.id.tvMensaje); // debe tener este ID en el XML

        AppDatabase db = AppDatabase.getInstance(this);
        Usuario usuario = db.usuarioDao().login("3201234567", "12345");

        if (usuario != null) {
            textView.setText("Hola " + usuario.nombre);
        } else {
            textView.setText("Usuario no encontrado");
        }
    }
}
