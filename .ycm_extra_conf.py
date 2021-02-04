import os
import ycm_core
import os.path as p

DIR_OF_THIS_SCRIPT = p.abspath( p.dirname( __file__ ) )
DIR_OF_THIRD_PARTY = p.join( DIR_OF_THIS_SCRIPT, 'third_party' )
DIR_OF_WATCHDOG_DEPS = p.join( DIR_OF_THIRD_PARTY, 'watchdog_deps' )


flags = [
        '-Wall',
        '-Wextra',
        '-Werror',
'-I',
'/home/cliff/pyworkspace/lf_xls/utils',
'-I',
'/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-3',
'-I',
'/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-2',
'-I',
'/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-1',
'-I',
'/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602',
'-I',
'/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602',
        ]

def Settings( **kwargs ):
    language = kwargs[ 'language' ]
    if language == 'python':
      client_data = kwargs[ 'client_data' ]
      return {
            'flags': flags,
            'interpreter_path': client_data[ 'g:ycm_python_interpreter_path' ],
            'sys_path': client_data[ 'g:ycm_python_sys_path' ]
            }
    return {
            'flags': flags,
            'include_paths_relative_to_dir': p.dirname( p.abspath( __file__ ) )
            }


def PythonSysPath( **kwargs ):
  sys_path = kwargs[ 'sys_path' ]

  interpreter_path = kwargs[ 'interpreter_path' ]

  sys_path[ 0:0 ] = [ p.join( DIR_OF_THIS_SCRIPT ),
p.join('/home/cliff/pyworkspace/lf_xls/utils'),
p.join('/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-3'),
p.join('/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-2'),
p.join('/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602/ST2-1'),
p.join('/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602/配置文件20200602'),
p.join('/home/cliff/pyworkspace/lf_xls/ST2注册检数据20200602'),
  ]

  sys_path.append( p.join( DIR_OF_THIRD_PARTY, 'jedi_deps', 'numpydoc' ) )
  return sys_path

