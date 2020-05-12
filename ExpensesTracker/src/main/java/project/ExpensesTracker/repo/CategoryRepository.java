package project.ExpensesTracker.repo;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import project.ExpensesTracker.domain.Category;

public interface CategoryRepository extends CrudRepository<Category, Long> {

	List<Category> findByName(String name);

}
