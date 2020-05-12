package project.ExpensesTracker.repo;

import org.springframework.data.repository.CrudRepository;

import project.ExpensesTracker.domain.User;

public interface UserRepository extends CrudRepository<User, Long> {
	User findByUsername(String username);
}
