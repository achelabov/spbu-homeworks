defmodule NumericalMethods do
  import :math, only: [exp: 1, sqrt: 1]
  alias :lists, as: Lists

  # Вариант 7
  def p(_x), do: 1

  def r(x), do: exp(-x)

  def f(x), do: x - x * x

  def q(_x), do: 0

  # Метод прогонки
  def tridiagonal_matrix_algorithm(k, f, n) do
    start_time = :os.system_time(:millisecond)
    s = :lists.duplicate(n - 2, 0)
    t = :lists.duplicate(n - 1, 0)
    y = :lists.duplicate(n - 1, 0)

    {s, t, y} = initialize_tridiagonal(k, f, s, t, n)

    for i <- 1..(n - 3) do
      s = List.replace_at(s, i, -k[i][i + 1] / (k[i][i] + k[i][i - 1] * s[i - 1]))
    end

    for i <- 1..(n - 2) do
      t = List.replace_at(t, i, (f[i][0] - k[i][i - 1] * t[i - 1]) / (k[i][i] + k[i][i - 1] * s[i - 1]))
    end

    y = List.replace_at(y, n - 2, t[n - 2])

    for i <- (n - 3)..0 do
      y = List.replace_at(y, i, s[i] * y[i + 1] + t[i])
    end

    work_time = :os.system_time(:millisecond) - start_time
    {y, work_time}
  end

  defp initialize_tridiagonal(k, f, s, t, n) do
    s = List.replace_at(s, 0, -k[0][1] / k[0][0])
    t = List.replace_at(t, 0, f[0][0] / k[0][0])
    {s, t, :lists.duplicate(n - 1, 0)}
  end

  # Метод Якоби
  def jacoby_method(k, g, err, max_num, n, sigma) do
    start_time = :os.system_time(:millisecond)
    u_new = :lists.duplicate(n - 1, 0)
    d = diagonal_inverse(k)
    u_old = :lists.duplicate(n - 1, 0)

    for _ <- 1..max_num do
      u_old = u_new
      u_new = Lists.zip_with(u_old, multiply(k, u_old) |> subtract(g), fn u, d -> u - sigma * d end)

      if norm(u_new, u_old) < err do
        break
      end
    end

    work_time = :os.system_time(:millisecond) - start_time
    {u_new, work_time}
  end

  defp diagonal_inverse(k) do
    Enum.map(k, fn row ->
      Enum.map(row, fn elem -> if elem != 0, do: 1 / elem, else: 0 end)
    end)
  end

  defp multiply(a, b) do
    for row <- a do
      for col <- transpose(b) do
        Enum.zip_with(row, col, &(&1 * &2)) |> Enum.sum()
      end
    end
  end

  defp subtract(a, b) do
    Enum.zip_with(a, b, &(&1 - &2))
  end

  defp norm(a, b) do
    a
    |> Enum.zip(b)
    |> Enum.map(fn {x, y} -> (x - y) * (x - y) end)
    |> Enum.sum()
    |> :math.sqrt()
  end

  defp transpose(matrix) do
    matrix
    |> Enum.zip()
    |> Enum.map(&Tuple.to_list/1)
  end

  # Матрицу коэффициентов
  def get_coef_matrix(p, r, f, n) do
    h = 1 / n
    b = :lists.duplicate(n - 1, 0)
    a = :lists.duplicate(n - 2, 0)
    k = :lists.duplicate(n - 1, :lists.duplicate(n - 1, 0))
    f_matrix = :lists.duplicate(n - 1, [0])

    for i <- 0..(n - 2) do
      f_matrix = List.replace_at(f_matrix, i, [f.(i * h + h) * h])
      b = List.replace_at(b, i, (2 / 3) * r.(i * h + h) * h + (p.(i * h + (0.5 * h)) + p.(i * h + (1.5 * h))) / h)
    end

    for i <- 0..(n - 3) do
      a = List.replace_at(a, i, (1 / 6) * r.(i * h + (1.5 * h)) * h - p.(i * h + (1.5 * h)) / h)
    end

    k = List.replace_at(k, 0, List.replace_at(k[0], 0, b))
    k = List.replace_at(k, 1, List.replace_at(k[1], 1, a))

    for i <- 1..(n - 2) do
      k = List.replace_at(k, i, List.replace_at(k[i], i, b))
      k = List.replace_at(k, i, List.replace_at(k[i], i - 1, a))
      k = List.replace_at(k, i, List.replace_at(k[i], i + 1, a))
    end

    {k, f_matrix}
  end

  # Получаем сигму
  def get_sigma(k, n) do
    h = 1 / n
    sum_of_elem = :lists.duplicate(n - 1, 0)
    sum_of_elem = List.replace_at(sum_of_elem, 0, k[0][0] + k[1][0])

    for j <- 1..(n - 3) do
      sum_of_elem = List.replace_at(sum_of_elem, j, k[j][j] + k[j - 1][j] + k[j + 1][j])
    end

    sum_of_elem = List.replace_at(sum_of_elem, n - 2, k[n - 2][n - 2] + k[n - 3][n - 2])
    2 / Enum.max(sum_of_elem)
  end

  # Метод декомпозиции
  def decomposition_method(k, f, err, max_num, n, sigma) do
    start_time = :os.system_time(:millisecond)
    m = trunc(sqrt(n))
    h = 1 / n

    # Формируем предобуславливатель
    delta_hh = :lists.duplicate(n - 1, :lists.duplicate(n - 1, 0))
    delta = :lists.duplicate(n - 1, :lists.duplicate(n - 1, 0))

    for i <- 0..(m * (m - 1) - 1) do
      delta = List.replace_at(delta, i, List.replace_at(delta[i], i, 2))
    end

    for i <- 0..(m * (m - 1) - 3) do
      delta = List.replace_at(delta, i, List.replace_at(delta[i], i + 1, -1))
      delta = List.replace_at(delta, i + 1, List.replace_at(delta[i + 1], i, -1))
    end

    delta = Enum.map(delta, fn row -> Enum.map(row, &(&1 / h)) end)

    for i <- (m * (m - 1))..(m * m - 2) do
      delta_hh = List.replace_at(delta_hh, i, List.replace_at(delta_hh[i], i, 2))
    end

    for i <- (m * (m - 1))..(m * m - 3) do
      delta_hh = List.replace_at(delta_hh, i, List.replace_at(delta_hh[i], i + 1,      -1))
      delta_hh = List.replace_at(delta_hh, i + 1, List.replace_at(delta_hh[i + 1], i, -1))
    end

    delta_hh = Enum.map(delta_hh, fn row -> Enum.map(row, &(&1 / (h * m))) end)
    delta_hh = Enum.zip_with(delta_hh, delta, fn a, b -> Enum.zip_with(a, b, &(&1 + &2)) end)

    p_arr = for i <- 0..100, do: p(i * (1 / 100))
    p_mean = Enum.sum(p_arr) / length(p_arr)
    delta_hh = Enum.map(delta_hh, fn row -> Enum.map(row, &(&1 * p_mean)) end)

    # Матрица преобразования
    c = matrix_transform(n)
    kdd = multiply(transpose(c), multiply(k, c))
    fdd = multiply(transpose(c), f)

    u_new = :lists.duplicate(n - 1, 0)
    u_old = :lists.duplicate(n - 1, 0)
    counter = 0

    for _ <- 1..max_num do
      u_old = u_new
      counter = counter + 1
      d_k = multiply(kdd, u_old) |> subtract(fdd)

      # Применяем метод прогонки
      {w_k, _} = tridiagonal_matrix_algorithm(delta_hh, sigma * d_k, n)
      u_new = Lists.zip_with(u_old, w_k, &(&1 - &2))

      if norm(u_new, u_old) < err do
        break
      end
    end

    u_new = multiply(c, u_new)
    work_time = :os.system_time(:millisecond) - start_time
    {u_new, work_time, counter}
  end

  defp matrix_transform(n) do
    m = trunc(sqrt(n))
    c = :lists.duplicate(n - 1, :lists.duplicate(n - 1, 0))

    for i <- 0..(n - 2) do
      c = List.replace_at(c, i, List.replace_at(c[i], i, 1))
    end

    kn = 1
    for i <- 0..((m - 1) * (m - 1) - 1) do
      c = List.replace_at(c, i, List.replace_at(c[i], m * (m - 1) + div(i, (m - 1)), kn / m))
      kn = kn + 1
      if kn == m, do: kn = 1
    end

    kn = m - 1
    for i <- m - 1..((m - 1) * m - 1) do
      c = List.replace_at(c, i, List.replace_at(c[i], m * (m - 1) + div(i, (m - 1)) - 1, kn / m))
      kn = kn - 1
      if kn == 0, do: kn = m - 1
    end

    c
  end

  # Основная часть программы
  def main do
    # Вызов функций
    n = IO.gets("Введите N: ") |> String.trim() |> String.to_integer()
    {k, f} = get_coef_matrix(&p/1, &r/1, &f/1, n)
    sigma = get_sigma(k, n)
    {y, work_time} = tridiagonal_matrix_algorithm(k, f, n)
    {y_j, work_time_j} = jacoby_method(k, f, 1e-4, 10000, n, sigma)

    xh = for i <- 1..(n - 1), do: i / n

    # n_decomp - количество элементов в сетке для метода декомпозиции
    n_decomp = 100
    {k1, f1} = get_coef_matrix(&p/1, &r/1, &f/1, n_decomp)
    {y_d, work_time_d, counter} = decomposition_method(k1, f1, 1e-4, 10000, n_decomp, sigma)
    xh_d = for i <- 1..(n_decomp - 1), do: i / n_decomp

    # Вывод таблицы значений
    IO.puts("N = #{n}:")
    IO.puts("Времена выполнения алгоритма:")
    IO.puts("Прогонка: #{work_time} Якоби: #{work_time_j} Декомпозиция: #{work_time_d} сек\n")
    IO.puts(String.pad_leading("x", 3) <> String.pad_leading("y(x)", 15) <>
      String.pad_leading("yJacoby(x)", 15) <> String.pad_leading("yDecomp(x)", 15))

    for i <- 1..9 do
      IO.puts(
        String.pad_leading(Float.to_string(i * 0.1, decimals: 1), 2) <>
        String.pad_leading(Float.to_string(y[(n * i) // 10], decimals: 12), 15) <>
        String.pad_leading(Float.to_string(y_j[(n * i) // 10], decimals: 12), 15) <>
        String.pad_leading(Float.to_string(y_d[(n_decomp * i) // 10], decimals: 12), 15)
      )
    end

    IO.puts("\n")
    IO.puts(String.pad_leading("№", 7) <> String.pad_leading("k1", 15) <>
      String.pad_leading("k2", 17) <> String.pad_leading("k3", 17) <> String.pad_leading("fi", 17))

    for i <- 1..9 do
      IO.puts(
        String.pad_leading(Integer.to_string((n * i) // 10), 4) <>
        String.pad_leading(Float.to_string(k[(n * i) // 10][(n * i) // 10], decimals: 12), 16) <>
        String.pad_leading(Float.to_string(k[(n * i) // 10][((n * i) // 10) - 1], decimals: 12), 16) <>
        String.pad_leading(Float.to_string(k[(n * i) // 10][((n * i) // 10) + 1], decimals: 12), 16) <>
        Float.to_string(f[(n * i) // 10][0], decimals: 12)
      )
    end

    IO.puts("Графики:")
    IO.puts("Метод прогонки N=#{n}")
    IO.inspect({xh, y})

    IO.puts("Метод Якоби N=#{n}")
    IO.inspect({xh, y_j})

    IO.puts("Метод декомпозиции N=#{n_decomp}")
    IO.inspect({xh_d, y_d})
  end
end

# Запуск основной программы
NumericalMethods.main()
