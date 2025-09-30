class animal = object
  method eat = print_endline "comiendo"
end;;

class mammal =object
inherit animal
method feed_offspring = print_endline "alimentando a los hijos"
end;;

class dog = object
inherit mammal
  method bark = print_endline "guau"
end;;

let maka = new dog;;

maka#eat;;
maka#feed_offspring;;
maka#bark;;