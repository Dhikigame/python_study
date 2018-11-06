#from package.module import User, AdminUser
import module

#mike = AdminUser("mike", 35)
mike = module.AdminUser("mike", 35)
print(mike.name)
print(mike.age)
mike.print_name()