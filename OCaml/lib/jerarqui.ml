class worker (name: string) (income: float ) = object

  val mutable name = name
  val mutable income = income
end;;

class chief(name: string) (income: float) = object
inherit worker name income
  method manage_team = print_endline "managing team"
end;;

class programmer(name: string) (income: float) = object
inherit worker name income
method code = print_endline "coding"
end;;

class account (name: string) (income: float) = object
inherit worker name income
method manage_accounts = print_endline "managing accounts"
end;;

let jessica = new chief "Jessica" 100.5;;
let fernando = new programmer "Fernando" 100.5;;
let maria = new account "Maria"

jessica#get_name;;
jessica#manage_team;;
jessica#get_income;;

fernando#get_name;;
fernando#manage_team;;
fernando#get_income;;

maria#get_name;;
maria#manage_team;;
maria#get_income;;