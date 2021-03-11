x <- c(67, 45, 92, 83, 70)

# 1
(67 - 32) * 5/9
(45 - 32) * 5/9
(92 - 32) * 5/9
(83 - 32) * 5/9
(70 - 32) * 5/9

(x - 32) * 5/9

# 2
convert_FC(x)

convert_FC <- function(temp_F) {
  result = (temp_F - 32) * 5/9
  return(result)
}


x <- c(1, 3, 9, 7, 1, 2, 2, 5, 3, 3, 3)
a <- c(1, 2, 3)


stat_mode <- function(data_vec) {
  my_table <- table(data_vec)
  
  result = names(sort(-my_table))[1]
  return(result)
}

stat_mode(x)

sort(-table(x))
