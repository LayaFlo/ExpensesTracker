package project.ExpensesTracker.web;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import project.ExpensesTracker.domain.Expense;
import project.ExpensesTracker.repo.CategoryRepository;
import project.ExpensesTracker.repo.ExpenseRepository;

@Controller
public class ExpenseController {
	@Autowired
	private ExpenseRepository repository;

	@Autowired
	private CategoryRepository crepository;

	@RequestMapping(value = "/login")
	public String login() {
		return "login";
	}

	@RequestMapping(value = "/")
	public String ExpensesTracker(Model model) {
		model.addAttribute("expenses", repository.findAll());
		return "expenselist";
	}

	@RequestMapping(value = "/expenselist")
	public String expenselist(Model model) {
		model.addAttribute("expenses", repository.findAll());
		return "expenselist";
	}

	@RequestMapping(value = "/add")
	public String addExpense(Model model) {
		model.addAttribute("expense", new Expense());
		model.addAttribute("categories", crepository.findAll());
		return "addexpense";
	}

	@RequestMapping(value = "/save", method = RequestMethod.POST)
	public String save(Expense expense) {
		repository.save(expense);
		return "redirect:expenselist";
	}

	@RequestMapping(value = "/delete/{id}", method = RequestMethod.GET)
	public String deleteExpense(@PathVariable("id") Long id, Model model) {
		repository.deleteById(id);
		return "redirect:../expenselist";
	}

	@RequestMapping(value = "/edit/{id}")
	public String addExpense(@PathVariable("id") Long expenseId, Model model) {
		model.addAttribute("expense", repository.findById(expenseId));
		model.addAttribute("categories", crepository.findAll());
		return "editexpense";
	}

	@RequestMapping(value = "/expenses", method = RequestMethod.GET)
	public @ResponseBody List<Expense> bookListRest() {
		return (List<Expense>) repository.findAll();

	}

	@RequestMapping(value = "/expense/{id}", method = RequestMethod.GET)
	public @ResponseBody Optional<Expense> findExpenseRest(@PathVariable("id") Long expenseId) {
		return repository.findById(expenseId);
	}
	
}
