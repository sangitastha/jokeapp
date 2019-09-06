<html>
<body>

 <?php 
  
  
  
  function tellmeajoke(){
    $array_of_jokes = array(
        "I used to think the brain was the most important organ. Then I thought, look what's telling me that.",
        "How does NASA organize their company parties? They planet.",
        "Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
        "I'm so good at sleeping. I can do it with my eyes closed.",
        "My boss told me to have a good day.. so I went home."
    );

   
      $length_of_array=count($array_of_jokes);
    $index_of_array = rand(0,$length_of_array-1);  
    $random_joke = $array_of_jokes[$index_of_array];

    return $random_joke;
    }
  

echo tellmeajoke();
?> 

</body>
</html>