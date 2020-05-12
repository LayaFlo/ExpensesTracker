package project.ExpensesTracker;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import project.ExpensesTracker.domain.Category;
import project.ExpensesTracker.domain.User;
import project.ExpensesTracker.repo.CategoryRepository;
import project.ExpensesTracker.repo.ExpenseRepository;
import project.ExpensesTracker.repo.UserRepository;

@SpringBootApplication
public class ExpensesTrackerApplication {

	public static void main(String[] args) {
		SpringApplication.run(ExpensesTrackerApplication.class, args);
	}
	@Bean
	public CommandLineRunner demo(ExpenseRepository repository, CategoryRepository crepository, UserRepository urepository) {
		return (args) -> {
			crepository.save(new Category("Entertaiment"));
			crepository.save(new Category("Electronic"));
			crepository.save(new Category("Groseries"));
			crepository.save(new Category("Pets"));
			
			//login: user password:user
			//login: admin password:admin
			User user1 = new User("user", "$2a$10$XxTUBwZHTOjbVDEaXlpBuO0VBKcAd89vN7Ptqwm30dWG7BhNzW7MW", "USER");
			User user2 = new User("admin", "$2a$10$oxgXtcq92.7xTtz24Wf/zeud0c/3/HN7zRJ0gyFuNiwar.n7IDXu6", "ADMIN");
			urepository.save(user1);
			urepository.save(user2);

		};
	}
}
