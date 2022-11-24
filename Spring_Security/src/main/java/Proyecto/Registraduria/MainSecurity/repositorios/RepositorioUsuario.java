package Proyecto.Registraduria.MainSecurity.repositorios;

import Proyecto.Registraduria.MainSecurity.modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
    @Query("{'correo':?0}")
    public Usuario getUserByMail(String correo);

    @Query("{'seudonimo':?0}")
    public Usuario getUserBySeudonimo(String seudonimo);
}