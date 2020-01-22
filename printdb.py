from PersistenceLayer.Repository import repo



def main():
    print('Activities')
    for act in repo.Activities.get_all():
        print(act)
    print('Coffee stands')
    for table in repo.Coffee_stands.get_all():
        print(table)
    print('Employees')
    for emp in repo.Employees.get_all():
        print(emp)
    print('Products')
    for prod in repo.Products.get_all():
        print(prod)
    print('Suppliers')
    for sup in repo.Suppliers.get_all():
        print(sup)
    print('\nEmployees report')
    for report in repo.Employees.get_emp_report():
        print(report)
    if len(repo.Activities.get_activities_report()) > 0:
        print('\nActivities')
        for rep in repo.Activities.get_activities_report():
            print(rep)


if __name__ == "__main__":
    main()
