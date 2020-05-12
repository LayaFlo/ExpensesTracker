package project.ExpensesTracker.repo;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import project.ExpensesTracker.domain.Expense;

public interface ExpenseRepository extends CrudRepository<Expense, Long> {
	List<Expense> findAll();
}