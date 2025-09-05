class person name (name: string) = object
  val mutable _name = name

  method get_name = _name
end;;

class student name (name: string) = object
  inherit person name
  method study =  print_endline (_name ^ "estudiando")
end;;

class teacher name (name: string)= object
  inherit person name
  method teach = print_endline " esta enseniando"
end;;

let emilio = new student "Emilio";;
emilio#study;;

let mag = new teacher "Mag";;
mag#teach;;