def disp_tool():
    tool_list = [ 'tool_vertical_and_horizontal_conversion' ,
                  'tool_give_timestamp' ,
                  'tool_delete_error_string' ,
                  ]

    print('---'*20)
    print('a All')
    for no, tool in enumerate(tool_list):
        print(no,tool)

    print('---'*20)
    return tool_list

if __name__ == '__main__':
    disp_tool()

