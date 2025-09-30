class swimmer = object
  method swim = print_endline "swimming"
end;;

class cyclist = object
  method cycle = print_endline "pedaleando"
  end;;

class runner = object
  method run = print_endline "logging in strava"
  end;;

class triathlete = object
  method compete = print_endline "compitiendo"
end;;

let t = new triathlete;;


let () = print_endline "el triatleta"
t#swim;;
t#pedal;;
t#run;;
t#compete;;