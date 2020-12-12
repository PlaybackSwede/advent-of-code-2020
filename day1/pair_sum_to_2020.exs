values = File.stream!("input.txt")
|> Stream.map(&String.trim_trailing/1)
|> Stream.map(&String.to_integer/1)
|> Enum.to_list

for x <- values, y <- values, x != y && x+y == 2020, do: IO.puts("#{x}*#{y} = #{x*y}")
