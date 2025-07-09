package com.example.primeraapp.db;

import android.content.Context;
import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

@Database(entities = {Usuario.class}, version = 1, exportSchema = false)
public abstract class AppDatabase extends RoomDatabase {

    private static final String DB_NAME = "bmis.db";
    private static AppDatabase instance;

    public abstract UsuarioDao usuarioDao();

    public static synchronized AppDatabase getInstance(Context context) {
        if (instance == null) {
            File dbFile = context.getDatabasePath(DB_NAME);

            if (!dbFile.exists()) {
                copyDatabaseFromAssets(context, dbFile);
            }

            instance = Room.databaseBuilder(context.getApplicationContext(),
                            AppDatabase.class, DB_NAME)
                    .createFromFile(dbFile)
                    .allowMainThreadQueries()  // Solo para pruebas
                    .build();
        }
        return instance;
    }

    private static void copyDatabaseFromAssets(Context context, File outFile) {
        try {
            InputStream input = context.getAssets().open(DB_NAME);
            outFile.getParentFile().mkdirs();
            OutputStream output = new FileOutputStream(outFile);
            byte[] buffer = new byte[1024];
            int length;
            while ((length = input.read(buffer)) > 0) {
                output.write(buffer, 0, length);
            }
            output.flush();
            output.close();
            input.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
