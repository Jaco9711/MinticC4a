package Proyecto.Registraduria.MainSecurity.repositorios;

import Proyecto.Registraduria.MainSecurity.modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol, String > {
}